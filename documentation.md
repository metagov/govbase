# Govbase Documentation

## API
The auto-generated Airtable API documentation can be found here: 

## Tables
Govbase is organized into three main tables: Projects, Organizations, and Structures.

| Table         | Description                                                       | Examples                                           |
|---------------|-------------------------------------------------------------------|----------------------------------------------------|
| Projects      | Platforms, software, and research in online governance            | Discourse, SourceCred, Open Collective, Aragon     |
| Organizations | Organizations and communities that develop, use, or fund projects | Enspiral, MetaGame, Knight Foundation              |
| Structures    | Concepts and institutions from social science; source of labels   | Quadratic voting, democracy, online community, DAO |

PROJECTS: A project is a discrete, re-usable software or research product. Includes code libraries, online platforms, online services, APIs, standards, protocols, and data sets.

ORGANIZATIONS: A (social) organization is an entity composed of individuals gathered for a common purpose. Includes online communities, companies, nonprofits, and funders involved in online governance.

STRUCTURES: A (governance) structure or institutional pattern is a scientific or technical description of a set of similar social behaviors and practices. Used mostly as a source of labels for PROJECTS.

### Projects
Each record in the Projects table contains the following fields:

#### Project
string
EXAMPLE VALUES
"1Hive Gardens"

"3Box"

"Abridged"

"ActivityPub"

"ActivityStreams 2.0"

#### Category
string

POSSIBLE VALUES
[
    "research",
    "product",
    "platform",
    "standard",
    "mashup"
]
DescriptionText
string
A single line of text.
 
EXAMPLE VALUES
"A technology stack to build and manage decentralized projects. No coding required."

"The ActivityPub protocol is a decentralized social networking protocol based upon the [ActivityStreams] 2.0 data format. It provides a client to serve..."

"This specification details a model for representing potential and completed activities using the JSON format. It is intended to be used with vocabular..."

"“the only 'always on' platform that works in both campaign and governance (coming soon) phases of government ensuring continuity amongst supporters an..."

"“the social network for e-democracy”"

WebsiteURL
string
A valid URL (e.g. airtable.com or https://airtable.com/universe).
 
EXAMPLE VALUES
"https://github.com/1Hive/gardens-template"

"https://3box.io/"

"https://abridged.io/"

"https://activitypub.rocks/"

"https://www.w3.org/TR/activitystreams-core/"

Legally owned by organization
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Organizations table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Funded by organization
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Organizations table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Online / offline
Single select
string
Selected option name.

When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match.

 
POSSIBLE VALUES
[
    "Online communities",
    "Offline communities",
    "Not specific"
]
ContactEmail
string
A valid email address.
 
EXAMPLE VALUES
"https://dustycloud.org/contact/"

"https://github.com/burrrata"

"legal@blockstack.org"

"kyle@kemitchell.com"

"https://commonsstack.org/community#contact"

Screenshot of UI
Attachment
array of attachment objects
Each attachment object may contain the following properties. To see which fields are required or optional, please consult the relevant section: retrieve, create, update, or delete.

idstring
unique attachment id
urlstring
url, e.g. "https://dl.airtable.com/foo.jpg"
filenamestring
filename, e.g. "foo.jpg"
sizenumber
file size, in bytes
typestring
content type, e.g. "image/jpeg"
widthnumberheightnumber
width/height, in pixels (these may be available if the attachment is an image)
thumbnails.small.urlstringthumbnails.large.urlstring
url of small/large thumbnails (these may be available if the attachment is an image or document)
thumbnails.small.widthnumberthumbnails.small.heightnumberthumbnails.large.widthnumberthumbnails.large.heightnumber
width/height of small/large thumbnails, in pixels (these will be available if the corresponding thumbnail url is available)
 
EXAMPLE VALUES
[
    {
        "id": "attIAK3vdyA04u0Rh",
        "url": "https://dl.airtable.com/.attachments/b6e5278c154714d66ff2e1893f4cb24e/620a5c0e/original.png",
        "filename": "original.png",
        "size": 190184,
        "type": "image/png",
        "thumbnails": {
            "small": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/a579a39917b48488da5453e956b99a44/87d018d6",
                "width": 64,
                "height": 36
            },
            "large": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/784790e7b5fab47203f5ad0bdc16e204/fcf3bcaf",
                "width": 720,
                "height": 405
            },
            "full": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/2cc49b24cff04288d55fb6453180f31b/7f5fba05",
                "width": 3000,
                "height": 3000
            }
        }
    }
]

[
    {
        "id": "attg7a6IDTCcFbgpV",
        "url": "https://dl.airtable.com/.attachments/cdd3a9d303912db8fe0c29247b70db1e/cf1795c8/homepage-2_optimized.jpg",
        "filename": "homepage-2_optimized.jpg",
        "size": 22541,
        "type": "image/jpeg",
        "thumbnails": {
            "small": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/3dd17b4780ca7baf6b7c4d8b2e1a65c5/c88d1422",
                "width": 73,
                "height": 36
            },
            "large": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/a4a4d879ca92a3d8899ed96080d0b744/f2e11160",
                "width": 950,
                "height": 471
            },
            "full": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/2227ec2f62f9b595b1ec92ce51aa7ae5/9cdeff0c",
                "width": 3000,
                "height": 3000
            }
        }
    }
]

Logo
Attachment
array of attachment objects
Each attachment object may contain the following properties. To see which fields are required or optional, please consult the relevant section: retrieve, create, update, or delete.

idstring
unique attachment id
urlstring
url, e.g. "https://dl.airtable.com/foo.jpg"
filenamestring
filename, e.g. "foo.jpg"
sizenumber
file size, in bytes
typestring
content type, e.g. "image/jpeg"
widthnumberheightnumber
width/height, in pixels (these may be available if the attachment is an image)
thumbnails.small.urlstringthumbnails.large.urlstring
url of small/large thumbnails (these may be available if the attachment is an image or document)
thumbnails.small.widthnumberthumbnails.small.heightnumberthumbnails.large.widthnumberthumbnails.large.heightnumber
width/height of small/large thumbnails, in pixels (these will be available if the corresponding thumbnail url is available)
 
EXAMPLE VALUES
[
    {
        "id": "attg2DtFJNtJpWfRq",
        "url": "https://dl.airtable.com/.attachments/062658ee524718b78ee9dcec04d68fa3/bb436e29/ActivityPub-logo.svg",
        "filename": "ActivityPub-logo.svg",
        "size": 18865,
        "type": "image/svg+xml",
        "thumbnails": {
            "small": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/f4c80fd72eaaeb6418b2615a8f303c98/f8809125.png",
                "width": 138,
                "height": 36
            },
            "large": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/980c3d4ea2686a0cee69699da2f64ba1/23ba9482.png",
                "width": 500,
                "height": 130
            },
            "full": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/54625e8a42ff4ad1874eba51f6728ef0/50f52770.png",
                "width": 3000,
                "height": 3000
            }
        }
    }
]

[
    {
        "id": "attEb5pWn0fFjIHA9",
        "url": "https://dl.airtable.com/.attachments/c3cf51856d10727924c9b3260309908e/26e78c42/7e352a0c-9e67-43aa-857f-18420307b456-1596730643159.png",
        "filename": "7e352a0c-9e67-43aa-857f-18420307b456-1596730643159.png",
        "size": 15261,
        "type": "image/png",
        "thumbnails": {
            "small": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/a59c62a6ff5c56625d94faef1ceba350/c213e8eb",
                "width": 69,
                "height": 36
            },
            "large": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/95e26972349d28fee2e2b070831af991/34381148",
                "width": 975,
                "height": 512
            },
            "full": {
                "url": "https://dl.airtable.com/.attachmentThumbnails/6772b52b7563bbcdf1a49a5c918b2aaf/db76a4a8",
                "width": 3000,
                "height": 3000
            }
        }
    }
]

Code repositoryURL
string
A valid URL (e.g. airtable.com or https://airtable.com/universe).
 
EXAMPLE VALUES
"https://github.com/1Hive/gardens-template"

"https://w3c.github.io/activitypub/"

"https://github.com/aragon/aragon"

"https://github.com/otwcode/otwarchive"

"https://github.com/Emberwalker/Arke"

Used by organization (staging for Instances)
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Organizations table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Contributed to by organization
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Organizations table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Uses project
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Projects table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Status
Single select
string
Selected option name.

When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match.

 
POSSIBLE VALUES
[
    "Dead",
    "Active",
    "Inactive",
    "Work in progress"
]
Wants interop with project
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Projects table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Implements structures
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Structures table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Project ownership type
Single select
string
Selected option name.

When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match.

 
POSSIBLE VALUES
[
    "Public research",
    "Open-source license",
    "Privately-owned",
    "Public domain copyright",
    "Open-core"
]
Is governed by (documentation)
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Documents table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

API or data modelURL
string
A valid URL (e.g. airtable.com or https://airtable.com/universe).
 
EXAMPLE VALUES
"https://www.w3.org/TR/activitypub/#obj"

"https://docs.blockstack.org/references/stacks-blockchain"

"https://discord.com/developers/docs/intro"

"https://docs.gitcoin.co/mk_rest_api/"

Year founded / first commitNumber
number
An integer (whole number, e.g. 1, 32, 99). This field only allows positive numbers.
 
EXAMPLE VALUES
2020

2016

2017

2016

2013

Instances
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Instances table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Tags
Multiple select
array of strings
Array of selected option names.

When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match.

 
POSSIBLE VALUES
[
    "DAO ecosystem",
    "blockchain ecosystem",
    "cities",
    "business collaboration software",
    "OSS ecosystem",
    "gaming ecosystem",
    "social networking",
    "research product",
    "dweb",
    "linked data/Semantic Web",
    "fediverse",
    "gig economy"
]
Subcategory
Multiple select
array of strings
Array of selected option names.

When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match.

 
POSSIBLE VALUES
[
    "programming language",
    "application protocol",
    "software library",
    "social network",
    "messaging platform",
    "forum platform",
    "debate platform",
    "publishing platform",
    "newsletter platform",
    "application/tool",
    "software framework",
    "online game",
    "data model/API",
    "blockchain",
    "crowdfunding platform",
    "recruiting/HR platform",
    "network protocol",
    "data set",
    "algorithm",
    "git platform",
    "service/API"
]
Link to license
Lookup
array of numbers, strings, booleans, or objects
Array of Original link fields in linked Documents records.
 
EXAMPLE VALUES
[
    "https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document"
]

[
    "https://github.com/blockstack/stacks-blockchain/blob/master/LICENSE"
]

[
    "https://github.com/discourse/discourse/blob/master/LICENSE.txt"
]

[
    "https://github.com/django/django/blob/master/LICENSE"
]

[
    "https://github.com/gitcoinco/web/blob/master/LICENSE"
]

Last modified by
Last modified by
collaborator object
Object providing details about the collaborator in this field.

idstring
unique user id
emailstring
user's email address
namestring
user's display name (optional, may be empty if the user hasn't created an account)
 
EXAMPLE VALUES
{
    "id": "usrgENXWVY04S1HCC",
    "email": "joshua.tan@magd.ox.ac.uk",
    "name": "Joshua Tan"
}

{
    "id": "usrgENXWVY04S1HCC",
    "email": "joshua.tan@magd.ox.ac.uk",
    "name": "Joshua Tan"
}

Data Sprint (August 27)
Checkbox
boolean
This field is "true" when checked and otherwise empty.
 
EXAMPLE VALUE
true

Used by project
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Projects table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Built interop with project
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Projects table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Involved in incidents
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Incidents table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Forked from project
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Projects table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Requires project (hard dependency)
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Projects table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]

Suggests project (soft dependency)
Link to another record
array of record IDs (strings)
Array of linked records IDs from the Projects table.
 
EXAMPLE VALUE
["rec8116cdd76088af", "rec245db9343f55e8", "rec4f3bade67ff565"]
