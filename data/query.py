from arango import ArangoClient
from pprint import pprint
import sys


degree_query = """
for n in nodes
  let edges = (
    for e in edges
      filter e._from == n._id
      return e
  )
  return {
    node: n,
    out_degree: length(edges)
  }
"""


def main():
    client = ArangoClient()
    db = client.db("similarity", username="root", password="letmein")

    cursor = db.aql.execute(degree_query)
    for row in sorted(cursor, key=lambda x: x["out_degree"], reverse=True):
        pprint(row)

    return 0


if __name__ == "__main__":
    sys.exit(main())
