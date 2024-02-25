#!/usr/bin/env python3
"""Task 34"""

from pymongo import MongoClient

def log_stats():
    """Provides some stats about Nginx logs stored in MongoDB"""

    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Total logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Check status
    check_status = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{check_status} status check")

if __name__ == "__main__":
    log_stats()
