from osmread import parse_file, Way

hillcenters = 0
for entity in parse_file('Rutgers Pathways.osm'):
    if isinstance(entity, Way) and 'name' in entity.tags:
        #Now we check what the name of a given Way is to see the way that represents the hill center
        #entity.tags (in this case Way.tags because we are choosing ways) is a dictionary with a 
        # variety of info about the particular way, print out an entity.tags to see all the info
        if entity.tags['name'] == "Hill Center Bldg For The Mathematical Sciences":
           hillcenters += 1

print("%s hill centers found" % hillcenters)
