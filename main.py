from fastapi import FastAPI , Depends , HTTPException, Query
from typing import Annotated
from sqlmodel import Session , select
from db import get_db , create_db_and_tables
from user import User , UserCreate , UserRead,  UserUpdate ,  Pin ,  PinCreate , PinUpdate , PinRead , Country , CountryCreate , CountryUpdate , CountryRead , Withdraw , WithdrawCreate , WithdrawUpdate , WithdrawRead , Package , PackageCreate , PackageUpdate , PackageRead , Referral , ReferralCreate , ReferralUpdate , ReferralRead 

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}


#get all users 

@app.get("/users" , response_model=list[User])
def get_users(session : Annotated[Session, Depends(get_db)], offset : int = Query(default=0 , le= 4), limit : int = Query(default=2 , le=4)):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users

#create users

@app.post("/users" , response_model=UserRead)
def create_user(user : UserCreate , session : Annotated[Session, Depends(get_db)]):
    user_to_insert = User.model_validate(user)
    session.add(user_to_insert)
    session.commit()
    session.refresh(user_to_insert)
    return user_to_insert

# get user by id
@app.get("/users/{user_id}" , response_model=UserRead)
def get_user_by_id(user_id : int , session : Annotated[Session, Depends(get_db)]):
    user = session.get(User , user_id)
    if not user:
        raise HTTPException(status_code=404 , detail="User not found")
    return user

# update user

@app.put("/users/{user_id}")
def update_user(user_id : int , user : UserUpdate , session : Annotated[Session, Depends(get_db)]):
    user_to_update = session.get(User , user_id)
    if not user_to_update:
        raise HTTPException(status_code=404 , detail="User not found")
    user_to_update.name = user.name
    user_to_update.email = user.email
    session.add(user_to_update)
    session.commit()
    session.refresh(user_to_update)
    return user_to_update

# delete user

@app.delete("/users/{user_id}")
def delete_user(user_id : int , session : Annotated[Session, Depends(get_db)]):
    user_to_delete = session.get(User , user_id)
    if not user_to_delete:
        raise HTTPException(status_code=404 , detail="User not found")
    session.delete(user_to_delete)
    session.commit()
    return {"message" : "User deleted"}


# get all pins

@app.get("/pins" , response_model=list[Pin])
def get_pins(session : Annotated[Session, Depends(get_db)], offset : int = Query(default=0 , le= 4), limit : int = Query(default=2 , le=4)):
    pins = session.exec(select(Pin).offset(offset).limit(limit)).all()
    return pins

# create pins

@app.post("/pins" , response_model=PinRead)
def create_pin(pin : PinCreate , session : Annotated[Session, Depends(get_db)]):
    pin_to_insert = Pin.model_validate(pin)
    session.add(pin_to_insert)
    session.commit()
    session.refresh(pin_to_insert)
    return pin_to_insert

# get by id pin

@app.get("/pins/{pin_id}" , response_model=PinRead)
def get_pin_by_id(pin_id : int , session : Annotated[Session, Depends(get_db)]):
    pin = session.get(Pin , pin_id)
    if not pin:
        raise HTTPException(status_code=404 , detail="Pin not found")
    return pin

# update pin

@app.put("/pins/{pin_id}")
def update_pin(pin_id : int , pin : PinUpdate , session : Annotated[Session, Depends(get_db)]):
    pin_to_update = session.get(Pin , pin_id)
    if not pin_to_update:
        raise HTTPException(status_code=404 , detail="Pin not found")
    pin_to_update.pin = pin.pin
    session.add(pin_to_update)
    session.commit()
    session.refresh(pin_to_update)
    return pin_to_update

# delete pin
@app.delete("/pins/{pin_id}")
def delete_pin(pin_id: int, session: Annotated[Session, Depends(get_db)]):
    pin_to_delete = session.get(Pin, pin_id)
    if not pin_to_delete:
        raise HTTPException(status_code=404, detail="Pin not found")
    session.delete(pin_to_delete)
    session.commit()
    return {"message": "Pin deleted"}

# get all country

@app.get("/countries" , response_model=list[Country])
def get_countries(session : Annotated[Session, Depends(get_db)], offset : int = Query(default=0 , le= 4), limit : int = Query(default=2 , le=4)):
    countries = session.exec(select(Country).offset(offset).limit(limit)).all()
    return countries

# create country

@app.post("/countries" , response_model=CountryRead)
def create_country(country : CountryCreate , session : Annotated[Session, Depends(get_db)]):
    country_to_insert = Country.model_validate(country)
    session.add(country_to_insert)
    session.commit()
    session.refresh(country_to_insert)
    return country_to_insert

# get by id country

@app.get("/countries/{country_id}" , response_model=CountryRead)
def get_country_by_id(country_id : int , session : Annotated[Session, Depends(get_db)]):
    country = session.get(Country , country_id)
    if not country:
        raise HTTPException(status_code=404 , detail="Country not found")
    return country

# update country

@app.put("/countries/{country_id}")
def update_country(country_id : int , country : CountryUpdate , session : Annotated[Session, Depends(get_db)]):
    country_to_update = session.get(Country , country_id)
    if not country_to_update:
        raise HTTPException(status_code=404 , detail="Country not found")
    country_to_update.name = country.name
    session.add(country_to_update)
    session.commit()
    session.refresh(country_to_update)
    return country_to_update

# delete country

@app.delete("/countries/{country_id}")
def delete_country(country_id : int , session : Annotated[Session, Depends(get_db)]):
    country_to_delete = session.get(Country , country_id)
    if not country_to_delete:
        raise HTTPException(status_code=404 , detail="Country not found")
    session.delete(country_to_delete)
    session.commit()
    return {"message" : "Country deleted"}

# get all referral

@app.get("/referrals" , response_model=list[Referral])
def get_referrals(session : Annotated[Session, Depends(get_db)], offset : int = Query(default=0 , le= 4), limit : int = Query(default=2 , le=4)):
    referrals = session.exec(select(Referral).offset(offset).limit(limit)).all()
    return referrals

# create referral

@app.post("/referrals" , response_model=ReferralRead)
def create_referral(referral : ReferralCreate , session : Annotated[Session, Depends(get_db)]):
    referral_to_insert = Referral.model_validate(referral)
    session.add(referral_to_insert)
    session.commit()
    session.refresh(referral_to_insert)
    return referral_to_insert

# get by id referral

@app.get("/referrals/{referral_id}" , response_model=ReferralRead)
def get_referral_by_id(referral_id : int , session : Annotated[Session, Depends(get_db)]):
    referral = session.get(Referral , referral_id)
    if not referral:
        raise HTTPException(status_code=404 , detail="Referral not found")
    return referral

# update referral

@app.put("/referrals/{referral_id}")
def update_referral(referral_id : int , referral : ReferralUpdate , session : Annotated[Session, Depends(get_db)]):
    referral_to_update = session.get(Referral , referral_id)
    if not referral_to_update:
        raise HTTPException(status_code=404 , detail="Referral not found")
    referral_to_update.referral = referral.referral
    session.add(referral_to_update)
    session.commit()
    session.refresh(referral_to_update)
    return referral_to_update

# delete referral

@app.delete("/referrals/{referral_id}")
def delete_referral(referral_id : int , session : Annotated[Session, Depends(get_db)]):
    referral_to_delete = session.get(Referral , referral_id)
    if not referral_to_delete:
        raise HTTPException(status_code=404 , detail="Referral not found")
    session.delete(referral_to_delete)
    session.commit()
    return {"message" : "Referral deleted"}

# get all package

@app.get("/packages" , response_model=list[Package])
def get_packages(session : Annotated[Session, Depends(get_db)], offset : int = Query(default=0 , le= 4), limit : int = Query(default=2 , le=4)):
    packages = session.exec(select(Package).offset(offset).limit(limit)).all()
    return packages

# create package

@app.post("/packages" , response_model=PackageRead)
def create_package(package : PackageCreate , session : Annotated[Session, Depends(get_db)]):
    package_to_insert = Package.model_validate(package)
    session.add(package_to_insert)
    session.commit()
    session.refresh(package_to_insert)
    return package_to_insert

# get by id package

@app.get("/packages/{package_id}" , response_model=PackageRead)
def get_package_by_id(package_id : int , session : Annotated[Session, Depends(get_db)]):
    package = session.get(Package , package_id)
    if not package:
        raise HTTPException(status_code=404 , detail="Package not found")
    return package

# update package

@app.put("/packages/{package_id}")
def update_package(package_id : int , package : PackageUpdate , session : Annotated[Session, Depends(get_db)]):
    package_to_update = session.get(Package , package_id)
    if not package_to_update:
        raise HTTPException(status_code=404 , detail="Package not found")
    package_to_update.name = package.name
    session.add(package_to_update)
    session.commit()
    session.refresh(package_to_update)
    return package_to_update

# delete package

@app.delete("/packages/{package_id}")
def delete_package(package_id : int , session : Annotated[Session, Depends(get_db)]):
    package_to_delete = session.get(Package , package_id)
    if not package_to_delete:
        raise HTTPException(status_code=404 , detail="Package not found")
    session.delete(package_to_delete)
    session.commit()
    return {"message" : "Package deleted"}

# get all withdraw

@app.get("/withdraws" , response_model=list[Withdraw])
def get_withdraws(session : Annotated[Session, Depends(get_db)], offset : int = Query(default=0 , le= 4), limit : int = Query(default=2 , le=4)):
    withdraws = session.exec(select(Withdraw).offset(offset).limit(limit)).all()
    return withdraws

# create withdraw

@app.post("/withdraws" , response_model=WithdrawRead)
def create_withdraw(withdraw : WithdrawCreate , session : Annotated[Session, Depends(get_db)]):
    withdraw_to_insert = Withdraw.model_validate(withdraw)
    session.add(withdraw_to_insert)
    session.commit()
    session.refresh(withdraw_to_insert)
    return withdraw_to_insert

# get by id withdraw

@app.get("/withdraws/{withdraw_id}" , response_model=WithdrawRead)
def get_withdraw_by_id(withdraw_id : int , session : Annotated[Session, Depends(get_db)]):
    withdraw = session.get(Withdraw , withdraw_id)
    if not withdraw:
        raise HTTPException(status_code=404 , detail="Withdraw not found")
    return withdraw

# update withdraw

@app.put("/withdraws/{withdraw_id}")
def update_withdraw(withdraw_id : int , withdraw : WithdrawUpdate , session : Annotated[Session, Depends(get_db)]):
    withdraw_to_update = session.get(Withdraw , withdraw_id)
    if not withdraw_to_update:
        raise HTTPException(status_code=404 , detail="Withdraw not found")
    withdraw_to_update.amount = withdraw.amount
    session.add(withdraw_to_update)
    session.commit()
    session.refresh(withdraw_to_update)
    return withdraw_to_update

# delete withdraw

@app.delete("/withdraws/{withdraw_id}")
def delete_withdraw(withdraw_id : int , session : Annotated[Session, Depends(get_db)]):
    withdraw_to_delete = session.get(Withdraw , withdraw_id)
    if not withdraw_to_delete:
        raise HTTPException(status_code=404 , detail="Withdraw not found")
    session.delete(withdraw_to_delete)
    session.commit()
    return {"message" : "Withdraw deleted"}










