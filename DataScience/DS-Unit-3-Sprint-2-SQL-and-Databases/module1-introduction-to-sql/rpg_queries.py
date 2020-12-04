import sqlite3
import pandas as pd


def connect_to_database(database):
    conn = sqlite3.connect(database)
    return conn



def main():
    database = r"rpg_db.sqlite3"
    answer1 = """
        SELECT COUNT() FROM charactercreator_character;"""
    answer2 = """
        SELECT COUNT(cc.character_id) as Character_Count
	    FROM 
		charactercreator_character cc
		JOIN charactercreator_mage cm 
			ON cc.character_id=cm.character_ptr_id
        UNION SELECT COUNT(cc.character_id)
	    FROM 
		charactercreator_character cc
		JOIN charactercreator_fighter cf
			ON cc.character_id=cf.character_ptr_id 
        UNION SELECT COUNT(cc.character_id)
	    FROM 
		charactercreator_character cc
		JOIN charactercreator_thief ct 
			ON cc.character_id = ct.character_ptr_id
        UNION SELECT COUNT(cc.character_id)
	    FROM 
		charactercreator_character cc
		JOIN charactercreator_cleric cl
			ON cc.character_id = cl.character_ptr_id
        UNION SELECT COUNT(cc.character_id)
	    FROM 
		charactercreator_character cc
		JOIN charactercreator_necromancer cn 
			ON cc.character_id = cn.mage_ptr_id;"""
    answer3 = """
        SELECT COUNT(item_id) 
        FROM armory_item;""" 
    answer4 = """
        SELECT COUNT()
        FROM armory_weapon;"""
    answer5 = """
        SELECT COUNT(item_id) as Item_Count,
        character_id
        FROM charactercreator_character_inventory
        GROUP BY character_id;"""
    answer6 = """
        SELECT COUNT(item_id) as weapon_count, character_id, item_ptr_id
        FROM charactercreator_character_inventory
        JOIN armory_weapon
        ON item_id = item_ptr_id
        GROUP BY character_id
        LIMIT 20;"""
    answer7 = """
        SELECT AVG(item_count) AS avg_inventory_amt
        FROM (
	        SELECT COUNT(cci.item_id) as item_count, cci.character_id 
	        FROM charactercreator_character_inventory cci
	        GROUP BY cci.character_id );"""
    answer8 = """
        SELECT AVG(item_count) AS avg_inventory_amt
        FROM (
	        SELECT COUNT(cci.item_id) as item_count, cci.character_id 
	        FROM charactercreator_character_inventory cci
	        JOIN armory_weapon aw 
	        ON cci.item_id = aw.item_ptr_id 
	        GROUP BY cci.character_id );"""
    ans = [answer1, answer3, answer4, answer5, answer6]
    conn = connect_to_database(database)
    curs = conn.cursor()
    for i in range(len(ans)):
        print(curs.execute(ans[i]).fetchall())

        
if __name__ == "__main__":
    main()