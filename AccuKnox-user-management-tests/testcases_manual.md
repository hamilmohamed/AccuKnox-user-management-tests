# Manual Test Cases - User Management

| ID | Test Scenario | Pre-conditions | Test Steps | Test Data | Expected Result |
|----|---------------|----------------|------------|-----------|-----------------|
| TC01 | Navigate to Admin Module | Logged in as Admin | 1. Login. 2. Click Admin. | Admin/admin123 | System Users page displayed |
| TC02 | Add New User | On System Users page | 1. Click Add. 2. Fill form. 3. Save. | ESS, Linda Anderson, username_x, Enabled, Password@123 | User saved & visible in search |
| TC03 | Search Newly Created User | User created | 1. Enter username 2. Search | username_x | User appears in table |
| TC04 | Edit User Details | User exists | 1. Search user 2. Edit 3. Save | edited_username | Changes saved & visible |
| TC05 | Validate Updated Details | User edited | 1. Search 2. Open 3. Verify fields | edited_username | Fields match updates |
| TC06 | Delete the User | User exists | 1. Search 2. Select 3. Delete 4. Confirm | username_x | User removed; search returns no results |
