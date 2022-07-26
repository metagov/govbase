# Constitutions of Web3

The Constitutions of Web3 data set, part of [Govbase](https://govbase.metagov.org) at [Metagov](https://metagov.org), consists of a number of constitutions written for DAOs (decentralized autonomous organizations), blockchain projects, and other online communities.

## Contributing

If you would like to upload a (raw) constitution for a given online community, please either fill out the form at [https://metagov.typeform.com/addconstitution](https://metagov.typeform.com/addconstitution) or directly submit a pull request to add a file to this folder, preferably as a .md file. Please make sure that the section titles are recognizable, and please include the following JSON metadata as a comment at the bottom of the file:

```json
{ 
  "@context": "https://constitutions.metagov.org",
  "type": "constitution",
  "title": "<title of the document>",
  "name": "<name of the DAO>",
  "daoURI": "<URI of daoURI, see EIP-4824>",
  "dateCreated": "<YYYY-MM-DD>",
  "dateModified": "<YYYY-MM-DD>",
  "previousConstitutionURI": "<URI>",
  "inForce": "<True, False>",
  "archived": "<YYYY-MM-DD>"
}
```

## What is a constitution?

Typically, a constitution articulates *goals*,  *values*, and *rights* within the context of an organization's *decision-making*. It will sometimes describe the decision-making process of that organization, as well as any important institutions within that process (e.g. a legislative body, a president, a treasurer).

Not sure if your governance document is a constitution? Constitutional rights and values are specified informally in all sorts of places: blog posts, manifestos, covenants, governance.md files, etc. If you have a question, please open an issue or submit a pull request, and we can help you figure it out. Some constitutional documents are very short (less than 10 sentences), while others are drafted by lawyers and span 20+ pages.

# Team members
Joshua Tan, Max Langenkamp, Anna Weichselbraun, Ann Brody, and Lucia Korpas

Please contact josh@metagov.org if you have any questions or are looking for help in writing your organization's constitution.
