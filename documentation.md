# Govbase Documentation v0.1

## API
The auto-generated Airtable API documentation can be found here: https://airtable.com/appx3e9Przn9iprkU/api/docs. To access the Airtable API, you will need an Airtable account and editor access to the base (Airtabl will generate a key for you).

## Tables
Govbase is organized into three main tables: **Projects**, **Organizations**, and **Structures**.

| Table         | Description                                                       | Examples                                           |
|---------------|-------------------------------------------------------------------|----------------------------------------------------|
| Projects      | Platforms, software, and research in online governance            | Discourse, SourceCred, Open Collective, Aragon     |
| Organizations | Organizations and communities that develop, use, or fund projects | Enspiral, MetaGame, Knight Foundation              |
| Structures    | Concepts and institutions from social science; source of labels   | Quadratic voting, democracy, online community, DAO |

**Projects**: A project is a discrete, re-usable software or research product. Includes code libraries, online platforms, online services, APIs, standards, protocols, and data sets.

**Organizations**: A (social) organization is an entity composed of individuals gathered for a common purpose. Includes online communities, companies, nonprofits, and funders involved in online governance.

**Structures**: A (governance) structure or institutional pattern is a scientific or technical description of a set of similar social behaviors and practices. Used mostly as a source of labels for **Projects**.

### Projects
Most fields in the **Projects** table are pretty straightforward.

*Year founded*: If not obvious, use year of first commit.

*Status*: A project is inactive if it has been at least 2 years since the last commit. It's dead if the code and/or service is no longer accessible.

*Online/offline*: is the project specifically intended for online communities or offline communities? If not clear, say "not specific". If it is not intended for either (e.g. Linux), say "Not community-related". Intended to distinguish online governance tools like SourceCred from primarily offline tools like Consul (this later category of tools often gets classified under the heading of "civic tech", e.g. https://civictech.guide/).

*Implements structures*: a function to the **Structures** table. This is meant as, "this project implements or helps implement a community or organization with these observed structures." Alternately: "after using this project, an organization will likely demonstrate these observed structures." So Aragon implements DAOs, CIVS implements voting, and so on.
 
*Category*: possible values are
2. "product": libraries, tools, applications, and even services
3. "platform": hosted applications that communities interact on
4. "standard": includes protocols and text standards. Communities can interact via protocols, but protocols aren't hosted like platforms are.
5. "mashup": mashup of several platforms or products. My prototypical example is [vTaiwan](https://info.vtaiwan.tw/).
1. "research" includes data sets (like Govbase!) and algorithms. It does NOT include papers.

*Legally owned by organization*: The owner controls decisions and changes about the project. If a project is open source, the "owner" is the owner of the repository who maintains access controls to the repository.

*Wants interop with project*: should be 

*Is governed by (documentation)*: requires an entry to be created first in the Documents table.

*Used by project*: a staging column for more precise ways in which two projects interact, i.e. *Requires project (hard dependency)*, *Suggests project (soft dependency)*, *Forked from project*, and *Built interop with project*

### Organizations

## Schema
![govbase_schema](https://github.com/thelastjosh/govbase/blob/master/govbase_schema.png)
