
from sqlmodel import Field, SQLModel, Relationship

class CountryBase(SQLModel):
    name: str

#country
class Country(CountryBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    country_users : list["User"] = Relationship(back_populates="country")

class CountryRead(CountryBase):
    id: int

class CountryCreate(CountryBase):
    pass

class CountryUpdate(CountryBase):
    name: str
#pin
class Base_pin(SQLModel):
    pin : str

class Pin(Base_pin, table=True):
    id: int = Field(default=None, primary_key=True)
    pin_users : list["User"] = Relationship(back_populates="pin")

class PinRead(Base_pin):
    id: int

class PinCreate(Base_pin):
    pass

class PinUpdate(Base_pin):
    pin : str

# withdraw

class Base_withdraw(SQLModel):
    username : str
    amount : str

class Withdraw(Base_withdraw, table=True):
    id: int = Field(default=None, primary_key=True)
    withdraw_users : list["User"] = Relationship(back_populates="withdraw")

class WithdrawRead(Base_withdraw):
    id: int

class WithdrawCreate(Base_withdraw):
    pass

class WithdrawUpdate(Base_withdraw):
    username : str
    amount : str

# package 

class Base_package(SQLModel):
    name : str

class Package(Base_package, table=True):
    id: int = Field(default=None, primary_key=True)
    package_users : list["User"] = Relationship(back_populates="package")

class PackageRead(Base_package):
    id: int

class PackageCreate(Base_package):
    pass

class PackageUpdate(Base_package):
    name : str

#referral 

class Base_referral(SQLModel):
    Username : str

class Referral(Base_referral, table=True):
    id: int = Field(default=None, primary_key=True)
    referral_users : list["User"] = Relationship(back_populates="referral")

class ReferralRead(Base_referral):
    id: int

class ReferralCreate(Base_referral):
    pass

class ReferralUpdate(Base_referral):
    Username : str

# user-role





#user
class Base_user(SQLModel):
    national_id : str
    email : str
    phone : str
    city : str
    currency : str
    date : str
    country_id : int | None = Field(default=None, foreign_key="country.id")
    pin_id : int | None = Field(default=None, foreign_key="pin.id")
    withdraw_id : int | None = Field(default=None, foreign_key="withdraw.id")
    package_id : int | None = Field(default=None, foreign_key="package.id")
    referral_id : int | None = Field(default=None, foreign_key="referral.id")


class User(Base_user, table=True):
    id: int = Field(default=None, primary_key=True)
    country : Country = Relationship(back_populates="country_users")
    pin : Pin = Relationship(back_populates="pin_users")
    withdraw : Withdraw = Relationship(back_populates="withdraw_users")
    package : Package = Relationship(back_populates="package_users")
    referral : Referral = Relationship(back_populates="referral_users")
    
    

class UserRead(Base_user):
    id: int

class UserCreate(Base_user):
    pass

class UserUpdate(Base_user):
    pass


   



   