from osmread import parse_file, Way

highway_count = 0
for entity in parse_file('Rutgers Pathways.osm'):
    if isinstance(entity, Way) and 'highway' in entity.tags:
        highway_count += 1

print("%d highways found" % highway_count)
print("yeet")