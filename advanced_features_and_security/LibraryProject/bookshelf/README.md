# Permissions and Groups Setup

## Custom Permissions

The `Book` model has the following custom permissions:
- `can_view`: Can view book
- `can_create`: Can create book
- `can_edit`: Can edit book
- `can_delete`: Can delete book

## Groups

The following groups have been set up with the corresponding permissions:
- `Editors`: `can_create`, `can_edit`
- `Viewers`: `can_view`
- `Admins`: `can_view`, `can_create`, `can_edit`, `can_delete`

## Views

The views in `bookshelf/views.py` have been updated to check for the appropriate permissions using the `@permission_required` decorator.

## Testing

Create test users and assign them to different groups. Log in as these users and attempt to access various parts of the application to ensure that permissions are applied correctly.