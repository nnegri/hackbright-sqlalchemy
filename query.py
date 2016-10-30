"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()
# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()
# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()
# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()
# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter((Brand.founded == 1903) & (Brand.discontinued == None)).all()
# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()
# Get all models whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()
# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = db.session.query(Model.name, Model.brand_name, 
                    Brand.headquarters).filter(Model.year == year).all()

    for model in model_info:
        print "Model: %s, Brand: %s, Headquarters: %s" % (model[0], model[1], model[2])

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     for brand in db.session.query(Brand).all():
        print "Brand: ", brand.name, "\nModels:\t"
        for model in brand.models:
            print model.name, "\t"

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
""" This query returns a query object. In order to return a brand object, or list
of brand objects, you must add .one(), .first() or .all() to the end of this query."""
# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
""" An association table connects two tables that do not neccessarily have a 
natural connection. While the db cannot tell the difference between this and a 
middle table, for the user the association table only has meaning as a connector
between two existing tables. The relationship managed is typically "many-to-many". """
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    
    newstr = '%' + mystr + '%'
    return Brand.query.filter(Brand.name.like(newstr)).all()


def get_models_between(start_year, end_year):
    
    return Model.query.filter((Model.year >= start_year) & (Model.year < end_year)).all()
