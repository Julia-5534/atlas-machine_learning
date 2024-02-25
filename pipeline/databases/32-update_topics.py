#!/usr/bin/env python3
"""Task 32"""

def update_topics(mongo_collection, name, topics):
    """Updates all topics of a school document based on the name"""
    result = mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
    return result.modified_count
