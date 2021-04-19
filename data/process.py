import json
import sys


def main():
    # Pull in data.
    datafile = sys.argv[1]
    with open(datafile) as f:
        data = json.loads(f.read())

    # Pull node list together.
    nodes = []
    for key, node in data["nodes"].items():
        node["_key"] = key
        nodes.append(node)

    # Pull edge list together.
    edges = []
    for start, end in data["edges"]:
        edges.append({
            "_from": f"nodes/{start}",
            "_to": f"nodes/{end}",
        })

    # Write out nodes.
    with open("nodes.json", "w") as f:
        f.writelines(json.dumps(row) + "\n" for row in nodes)

    # Write out edges.
    with open("edges.json", "w") as f:
        f.writelines(json.dumps(row) + "\n" for row in edges)

    return 0


if __name__ == "__main__":
    sys.exit(main())
