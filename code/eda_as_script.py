# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import numpy as np
import pandas as pd
import networkx as nx

import matplotlib.pyplot as plt


# %%
import airtable as at
import json


# %%
with open('api.json') as json_file:
    ak = json.load(json_file)


# %%
api_key = ak['key']
base_key = "appx3e9Przn9iprkU"
organizations_table = "Organizations"
projects_table = "Projects"


# %%
orgs = at.Airtable(base_key, organizations_table, api_key)
org_fields = ["Uses project (staging for Instances)", "Organization name"]
daos = orgs.get_all(view = 'DAOs in the Wild',sort ='Organization name', fields = org_fields)

projs = at.Airtable(base_key, projects_table, api_key)
proj_fields = ["Project name"]
tools = projs.get_all(view = 'OSS Governance', sort ='Project name', fields = proj_fields)


# %%
daos[0]


# %%
tools[0]


# %%
daos[0]['fields']['Uses project (staging for Instances)']


# %%
for d in daos[:3]:
    print(d)
    print(d['fields']['Uses project (staging for Instances)'])
    print(len(d['fields']['Uses project (staging for Instances)']))
    print('')


# %%
#trim the data set and get a list of DAOs based on which ones have tool use data
my_daos = []
my_tool_ids = []
for d in daos:
     if 'Uses project (staging for Instances)' in d['fields'].keys():
         my_dao_id = d['id']
         my_dao_name = d['fields']['Organization name']
         my_dao_tools = d['fields']['Uses project (staging for Instances)']

         my_dao_record = {'id':my_dao_id, 'name':my_dao_name, 'tools':my_dao_tools }

         my_daos.append(my_dao_record)

         for t in my_dao_tools:
             if t not in my_tool_ids:
                 my_tool_ids.append(t)


# %%
my_tools = []

for t in tools:
    if t['id'] in my_tool_ids:
        my_tool_id = t['id']
        my_tool_name = t['fields']['Project name']

        my_tool_record = {'id':my_tool_id, 'name':my_tool_name}

        my_tools.append(my_tool_record)


# %%
my_tools


# %%
#DAOs as a dataframe
ddf = pd.DataFrame(my_daos)
tdf = pd.DataFrame(my_tools)


# %%
tdf.head()


# %%
#initialize a networkx object
G = nx.DiGraph()

#method to add a tool
def add_tool(g, r):
    '''
    g is networkx DiGraph()
    r is a record from the my_tools
    '''
    nid = r['id']
    g.add_node(nid)
    
    g.nodes[nid]['type']='tool'
    g.nodes[nid]['name'] = r['name']

#method to add an org (and tools it uses)
def add_org(g, r, tool_airtable = projs):
    '''
    g is networkx DiGraph()
    r is a record from my_daos
    '''
    nid = r['id']
    g.add_node(nid)
    
    g.nodes[nid]['type']='org'
    g.nodes[nid]['name'] = r['name']

    tids = r['tools']

    for tid in tids:
        if tid in g.nodes:
            g.add_edge(nid, tid)
            g.edges[nid,tid]['type'] = 'user'
        else:
            g.add_node(tid)
            g.nodes[tid]['type']='tool'

            t_data = tool_airtable.get(tid)

            g.nodes[tid]['name'] = t_data['fields']['Project name']

for d in my_daos:
    add_org(G, d)


# %%
G.nodes


# %%
def get_nodes_by_type(g, node_type_selection):
    '''
    Definition:
    Function to extract nodes based by named type
    Parameters:
    g: network x object
    node_type_selection: node type
    Assumptions:
    Returns:
    List column of the desired information as:
    Example:
    proposals = get_nodes_by_type(network, 'proposal')
    '''
    return [node for node in g.nodes if g.nodes[node]['type']== node_type_selection ]


# %%
dao_nodes = get_nodes_by_type(G, 'org')
n = len(dao_nodes)

tool_nodes = get_nodes_by_type(G, 'tool')
m = len(tool_nodes)


# %%
pos = {}
labels = {}

for i in range(n):
    d = dao_nodes[i]
    pos[d] = [0, i]

    try:
        labels[d] = G.nodes[d]['name']
    except:
        labels[d] = d

for j in range(m):
    t = tool_nodes[j]
    pos[t] = [1, j+(n-m)/2]

    try:
        labels[t] = G.nodes[t]['name']
    except:
        labels[t] = t


# %%
plt.figure(figsize=(12, 18))
nx.draw(G, pos, labels=labels, edge_color = 'gray')
plt.title('Graph View of Tools Used by DAOs in the Wild')

# null.tpl [markdown]
# ## Next steps
# - exploratory data analysis on this data steps

# %%
def includes(list, tool):
    return bool(tool in list)


# %%
aragon_tool_id = 'recTLikaQcam7XT6J'
ddf['aragon'] = ddf.tools.apply(lambda x: includes(x, aragon_tool_id))


# %%
orgs_using_aragon = ddf[ddf.aragon].id.values


# %%
len(orgs_using_aragon)


# %%
co_use = []
for l in ddf[ddf.aragon].tools.values:
    co_use = l + co_use

co_use = list(set(co_use))


# %%
len(co_use)


# %%
asg_nodes = list(orgs_using_aragon)+co_use
asg = G.subgraph(asg_nodes)


# %%
asg_labels = {}
for k in labels.keys():
    if k in asg_nodes:
        asg_labels[k] = labels[k]


# %%
plt.figure(figsize=(12, 18))
nx.draw_circular(asg, labels=asg_labels, edge_color = 'gray')
plt.title('Graph View of Tools Used by DAOs in the Wild')


# %%
list(ddf[ddf.id == 'recxhL8QqbWOKzwu8'].tools.values)[0]


# %%
ddf[ddf.id == 'recxhL8QqbWOKzwu8'].tools.values


# %%
co_use


# %%
ano = len(orgs_using_aragon)
ant = len(co_use)

data = np.empty((ano,ant))
for i in range(ano):
    org = orgs_using_aragon[i]
    use = list(ddf[ddf.id == org].tools.values)[0]
    print(org)
    print(use)
    for j in range(ant):
        tool = co_use[j]
        data[i,j] = bool(tool in use)



# %%



# %%
plt.spy(data.T)


# %%
def getnames(node_ids):
    print(node_ids)
    return [G.nodes[node_id]['name'] for node_id in node_ids]


# %%
plt.figure(figsize=(8, 4))
plt.bar(getnames(co_use),np.sum(data, axis = 0))
plt.xticks(rotation='vertical')


# %%
G.nodes[aragon_tool_id]['name']


# %%
plt.figure(figsize=(4, 8))
plt.barh(getnames(orgs_using_aragon),np.sum(data, axis = 1))


# %%
data_df = pd.DataFrame(data, index = getnames(orgs_using_aragon), columns=getnames(co_use) )


# %%
import seaborn as sns


# %%
sns.clustermap(data=data_df, cmap = 'Purples')


# %%
#normalized
#org_data = np.matmul(data,data.T)/np.sum(data, axis=1)

#unnormalized
org_data = np.matmul(data,data.T)

org_data_df = pd.DataFrame(org_data, index = getnames(orgs_using_aragon), columns=getnames(orgs_using_aragon) )
sns.clustermap(data=org_data_df, cmap = 'Purples')

# %%

#normalized
#tool_data = np.matmul(data.T,data)/np.sum(data, axis=0)
#unnormalized
tool_data = np.matmul(data.T,data)


tool_data_df = pd.DataFrame(tool_data, index = getnames(co_use), columns=getnames(co_use) )
sns.clustermap(data=tool_data_df, cmap = 'Purples')
# %%

