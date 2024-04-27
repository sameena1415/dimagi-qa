Referrals Outgoing Referrals
=================
This test will select a "referral" case and upon form submission, essentilaly "close" the case and
not available for selection on the next iteration. Therefore, this test requires a setting up
a large enough set of cases for each user such that the case list is not exhaused during the test.

The "Referrals Search for Beds" test script will create cases that will be consumed by this test. So
running the that test first could suffice. Alternately, "referral" cases can be imported with case property
"current_status" set to "open".

Central Registry Search and Admit
=================
This test will select a "client" case. These cases will not be consumed during the test so it only needs
to be set up once for the domain. See "client-cases-import-example" for a template on how to define the
cases to be imported then follow case import [instructions](https://dimagi.atlassian.net/wiki/spaces/commcarepublic/pages/2143946828/Importing+Cases+Using+Excel#When-Should-I-Use-the-Case-Importer?).