from typing import List, Optional
import datetime
import bson
from data.owners import Owner


def create_account(name, email, background, publications, grants, awards, teaching) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email
    owner.Department = background
    owner.publication = publications
    owner.grants = grants
    owner.awards = awards
    owner.teaching = teaching
    owner.save()
    return owner

def create_account_by_flask(name, email, department, password) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email
    owner.Department = department
    owner.password = password
    owner.save()
    return owner



def find_account_by_email_and_password(email: str, password: str) -> Owner:
    owner = Owner.objects(email=email, password = password).first()
    return owner


def find_account_by_email(email: str) -> Owner:
    owner = Owner.objects(email=email).first()
    return owner


def getInfo(user_id: bson.ObjectId):
    owner = Owner.objects(id=user_id).first()
    info = [] 
    info.append(owner.background)
    info.append(owner.publication)
    info.append(owner.grants)
    info.append(owner.awards)
    info.append(owner.teaching)
    return info


