# 2-14 Test Cases

## Test Case Format

Each test case must include:

- Test case ID
- Feature
- Preconditions
- Test steps
- Expected result
- Actual result
- Status: Passed or Failed
- Screenshot reference

## Required Functional Test Cases

1. Application starts successfully.
2. Main page opens without errors.
3. User can create a new record.
4. User can view a list of records.
5. User can open record details.
6. User can edit an existing record.
7. User can delete or archive a record.
8. Required fields are validated.
9. Invalid data is rejected.
10. Search or filtering works if implemented.

## Required Technical Test Cases

1. Docker containers start successfully.
2. Database connection works.
3. Database schema is created automatically.
4. Seed data is loaded.
5. Application can be restarted without losing database data.

## Required Security Test Cases

1. Passwords or secrets are not committed to GitHub.
2. User input is validated.
3. Error messages do not expose stack traces.
4. User roles are checked where roles are implemented.
