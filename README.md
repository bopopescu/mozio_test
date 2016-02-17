# Mozio Providers API

Full API documentation can be found at: http://docs.mozioapitest.apiary.io/

A Postman collection with all API end points to test locally is available at: https://www.getpostman.com/collections/ba9a4dbc57007120f329

## Assumptions

It's assumed that a Provider might define a Service Area as multiple geographical areas, that's why the usage of `MultiPolygonField`.

Currency format is defined in ISO_4217 format (https://en.wikipedia.org/wiki/ISO_4217) with a max of 3 characters.

Phone is assumed as international number, without specific format.
