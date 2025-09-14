class User:
    """Represents a user in the application."""

    is_admin = False
    is_moderator = False

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def create_admin(cls, username, email):
        """Creates a new admin user."""
        admin = cls(username, email)
        admin.is_admin = True
        print(f"Admin user '{username}' created.")
        return admin

    @classmethod
    def create_moderator(cls, username, email):
        """Creates a new moderator user."""
        moderator = cls(username, email)
        moderator.is_moderator = True
        print(f"Moderator user '{username}' created.")
        return moderator
    
    def display_status(self):
        """Displays the user's status."""
        status = "regular"
        if self.is_admin:
            status = "admin"
        elif self.is_moderator:
            status = "moderator"
        print(f"User: {self.username}, Status: {status}")

# Create users using the class methods
admin_user = User.create_admin("jdoe", "jdoe@example.com")
moderator_user = User.create_moderator("mmiller", "mmiller@example.com")

# The default constructor can still be used for a regular user
regular_user = User("greg_s", "greg@example.com")

print("\n--- User Status ---")
admin_user.display_status()
moderator_user.display_status()
regular_user.display_status()

