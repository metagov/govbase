# Pocket DAO Launch Roadmap

These milestones may not necessarily be achieved in the following order, depending on when their prerequisites are met.

## Tools Needed to Participate
 * Pocket CLI
 * Discord
 * Discourse
 * Aragon-compatible Ethereum wallet (MetaMask, Frame, Fortmatic, or Portis)
 * Rinkeby ETH

## 1: Seeding the DAO

### Target Dates:
Mainnet launch (July 28th)

### Prerequisites:
None

### Steps / Available Actions:
 * Initialize the Council with 5 founding Voters, who will each be assigned a VOTE in Aragon and be required to send 1,000 POKT (their Governance Stake) to the DAO treasury
 * Assign these founding Voters the role of Champion as well, which means they can vouch for new Voters and vote in new Champions
 * The first action of the Council will be voting unanimously to ratify the Constitution. No other action can be voted on until this has taken place

## 2: Growing the Seed

### Target Dates:
July 29th - October 1st

### Prerequisites:
Seeded DAO

### Steps / Available Actions:
 * Champions only can bring in new Voters, up to a cap of 50 Voters
 * All Voters must send 1,000 POKT (their Governance Stake) to the on-chain DAO treasury
 * The Governance Stake maturation requirement will not be active during this phase. The DAO can pass a majority vote at any time to activate the maturation requirement
 * The Council can begin voting on proposals, which anyone can submit; these will include Pocket Improvement Proposals (PIPs) such as protocol upgrades, Pocket Ecosystem Proposals (PEP) such as grant requests, and Parameter Update Proposals (PUPs) such as changes to the unstaking time

## 3: Sufficiently Decentralized

### Target Dates:
September 1st

### Prerequisites:
 * There are at least 100 independently operated Nodes
 * The Council has passed its first vote (and is therefore in Phase 2)

### Steps / Available Actions:
 * The App and Node UnstakingTime parameters will be changed from 21 days to 1 hour, subject to Majority Approval from Voting Token holders (50% yes votes)

## 4: Opening the Voter Set

### Target Dates:
October 1st

### Prerequisites:
Maxed-out Seed

### Steps / Available Actions:
 * All members of the Pocket Network community can now join the Council by sending POKT (a Governance Stake) to the on-chain DAO treasury, writing in the tx memo the Ethereum address they’ll be using in Aragon and their Discord username. Their stake will be one of 2 options:
   * **Trust-Minimized Stake:** they have not yet proven themselves trustworthy, so they must stake the value of the DAO treasury divided by the number of Voting Token holders in the Aragon organization (we expect this to be an unpopular option until the Council has scaled and this stake becomes cheaper)
   * **Trusted Stake:** they find a Champion who will mint their voting token for them, or they reach Elite level in the Pocket Community Game, entitling them to a stake of 1,000 POKT
 * Champions can vote in new Champions as another way to scale up the rate of new Voter admission

## 5: Gamified Access

### Target Dates:
October 1st (Q4)

### Prerequisites:
The Pocket Community Game (a series of gamified community quests) has been finalized by Pocket Network Inc

### Steps / Available Actions:
 * Pocket Network Inc will introduce the Game as an alternative route for community members to gain access to the Trusted Stake
 * Community members will begin playing the game and applying for Trusted Stakes once they have reached the necessary level (tentatively Elite)

## 6: Economic Signaling

### Target Dates:
TBD, dependent on Aragon releases

### Prerequisites:
 * Conviction Voting apps available on Aragon Chain mainnet
 * Rate of growth of the Block Reward has been negative for a continuous period of 7 days

### Steps / Available Actions:
 * Pocket Network Foundation will install Conviction Voting apps for the USDRelayTargetRange and ReturnOnInvestmentTarget parameters
 * Using these apps, the Council will begin actively and continuously signaling what they believe the value of these parameters should be

## 7: Peer Moderation

### Target Dates:
TBD, dependent on Aragon releases

### Prerequisites:
Aragon Agreements app and Aragon Court are available on Aragon Chain mainnet

### Steps / Available Actions:
 * Pocket Network Foundation will configure a new Aragon organization, replacing the Aragon Approvals app (centralized moderation) with the Aragon Agreements app (decentralized moderation), then copy the token distribution over
 * Using the Agreements app, the Council will be able to challenge each other’s actions and take a more active role in enforcing the Constitution

## 8: Re-evaluating the Champion System

### Target Dates:
January 1st, subject to the Game start date and season length

### Prerequisites:
The Pocket Community Game has been in operation for one full season

### Steps / Available Actions:
A supermajority vote will be held on whether the Champion system is still needed in light of gamified access being operational (50% yes/no votes)

## 9: Custom Governance Dashboard

### Target Dates:
March 1st

### Prerequisites:
 * Aragon Connect
 * Internal developer resources or DAO contributors

### Steps / Available Actions:
Pocket Network Inc, the DAO, or both in collaboration, will build a custom governance dashboard that integrates Aragon, Pocket Network, Discord, Discourse, GitHub, and any other relevant governance tools, into a unified interface with a frictionless governance UX

## 10: Chat-native Interactions

### Target Dates:
TBD, dependent on available tooling

### Prerequisites:
 * Aragon Connect custom bot implementations
 * Abridged (or similar) out-of-the-box bots
 * Linking Discord accounts to Aragon, e.g. through Discord crypto wallets like Mule

### Steps / Available Actions:
Pocket Network Inc will roll out bots in the Discord server, which enable voting/proposing/challenging from within chat

## 11: Automating the DAO

### Target Dates:
TBD, dependent on technical research

### Prerequisites:
Technical achievements enabling an Aragon Agent to submit transactions to the Pocket Network (or equivalent cross-chain transactions)

### Steps / Available Actions:
Pocket Network Foundation will configure the Aragon organization with the necessary tooling, then update the ACL with the necessary permissions, subject to supermajority approval by the Council and the compliance requirements outlined in the Constitution

## 12: Decentralizing Community Admin

### Target Dates:
TBD, dependent on available tooling

### Prerequisites:
The ability for an Aragon DAO to assign, or approve the assignment of roles in Discord (or an equivalent community hub)

### Steps / Available Actions:
Pocket Network Inc will configure the Discord server, and Pocket Network Foundation will configure the Aragon organization, as is needed to facilitate decentralizing the admin of the Discord server (or equivalent community hub)
