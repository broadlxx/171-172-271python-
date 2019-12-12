print("XueXiang_Lv 175150 19023249")
import random
description = ['First', 'Dream', 'New Family', 'Brand New']    #
adjective = ['Wonderful', 'Sunny', 'Spacious', 'Secluded']
bedrooms = [1, 2, 3, 4, 5]
City = ['Tianjin','Baoding','Shijiazhuang','Tangshan','Chengde']
type_of_owner = ['a couple', 'a family', 'a retired couple','a large family', 'a professional couple']
amenities_close_by = ['great schools', 'shopping centre', 'motorway', 'airport', 'hospital']
print("*** Your "+ random.choice(description)+ " Home *** ")
print( random.choice(adjective)," ",random.choice(bedrooms)," bedroom home in ", random.choice(City))
print("Would suit "+random.choice(type_of_owner))
print("Close to "+random.choice(amenities_close_by))
print("All enquires to Joe on 183-0027-1234.")
print("*** Make it yours today! *** ")
