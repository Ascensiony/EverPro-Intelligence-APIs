from .competition_track import amazon_track_competition
import json
import time
import os


def load():
    with open(
        "./competition_tracking/api/competition_tracker.json", "r", encoding="utf-8"
    ) as f:
        return json.load(f)


def write(db):
    with open(
        "./competition_tracking/api/competition_tracker.json", "w", encoding="utf-8"
    ) as f:
        json.dump(db, f, ensure_ascii=False, indent=4)


def GET_CT(asin="all"):

    try:
        db = load()

        if asin == "all":
            return db

        to_return = []

        for data in db:
            if data["asin"] == asin:
                return data

    except Exception as e:
        print(e)
        return dict(error="Some internal error occurred", code=500)

    return dict(error="No records found", code=404)


def POST_CT_DATA(data: dict):

    try:
        db = list(load())

        for track_obj_i in db:
            if track_obj_i["asin"] == data["asin"]:
                return dict(error="Object already exists", code=409)

        db.append(dict(asin=data["asin"], zone=data["zone"]))
        write(db)

        return dict(success="Object created", code=200)

    except Exception as e:
        print(e)
        return dict(error="Some internal error occurred", code=500)

    return dict(error="Report to us.. this should not happen", code=500)


def POST_CT(data: dict):

    try:
        if type(data) == type([]):
            for d in data:
                return POST_CT_DATA(d)

        elif type(data) == type(dict()):
            return POST_CT_DATA(data)

        else:
            return dict(error="Bad Request", code=400)

    except Exception as e:
        print(e)
        return dict(error="Some internal error occurred", code=500)


def PUT_CT(data: dict):
    try:
        db = list(load())

        for track_obj_i in db:
            if track_obj_i["asin"] == data["asin"]:
                return dict(success="Object Updated", code=200)

        POST_CT(data)
        return dict(success="Object Created", code=200)

    except Exception as e:
        print(e)
        return dict(error="Some internal error occurred", code=500)


def DELETE_CT_DATA(data: dict):

    try:
        db = list(load())

        for index, track_obj_i in enumerate(db):
            if track_obj_i["asin"] == data["asin"]:
                del db[index]
                break

        write(db)
        return dict(success="Object deleted", code=200)

    except Exception as e:
        print(e)
        return dict(error="Some internal error occurred", code=500)

    return dict(error="Bad Request", code=400)


def DELETE_CT(data: dict):

    try:
        if type(data) == type([]):
            for d in data:
                return DELETE_CT_DATA(d)

        elif type(data) == type(dict()):
            return DELETE_CT_DATA(data)

        else:
            return dict(error="Bad Request", code=400)

    except Exception as e:
        print(e)
        return dict(error="Some internal error occurred", code=500)


# print(GET_CT_DATA(asin="abz"))
# print(POST_CT(dict(asin="zzzzz", zone="IN")))
# print(DELETE_CT(dict(asin="zzzzz", zone="IN")))
# print(amazon_track_competition("B07WSHWNH8", "IN"))