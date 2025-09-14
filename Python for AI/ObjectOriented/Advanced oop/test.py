class User:
    """Represent a user in the application"""
    is_admin = False
    is_moderator = False

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def create_admin(cls, username, email) :
        Admin = cls(username, email)
        Admin.is_admin = True
        print(f"{Admin.username} is succesfully created as a admin user")
        return Admin

    @classmethod
    def create_moderator(cls, usernamem, email) :
        """Create a new mod"""
        Moderator = cls(usernamem, email)
        Moderator.is_moderator = True
        print(f"Mod user has been created {usernamem}")
        return Moderator

    def get_status(self) :
        status = "regular"
        if self.is_admin :
            print(f"status : Admin")
        elif self.is_moderator:
            print(f"status : Moderator")
        else :
            print("status : regular")            

admin = User.create_admin("Dexter", "BayHourbar@gmail.com")
mod = User.create_moderator("Dokes", "miamimetro@gmail.com")

regular_user = User("greg_s", "greg@example.com")

print("\n--- User Status ---")
admin.get_status()
mod.get_status()
regular_user.get_status()