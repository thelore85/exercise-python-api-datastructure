
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""


from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            { 'first_name': 'lorenzo', 'age': 38, 'last_name': last_name, 'id': 1, 'lucky_numbers':[1,2,3,4,5]},            
            { 'first_name': 'lorenzo', 'age': 38, 'last_name': last_name, 'id': 2, 'lucky_numbers':[1,2,3,4,5]}, 
            { 'first_name': 'lorenzo', 'age': 38, 'last_name': last_name, 'id': 3, 'lucky_numbers':[1,2,3,4,5]}, 
            { 'first_name': 'lorenzo', 'age': 38, 'last_name': last_name, 'id': 4, 'lucky_numbers':[1,2,3,4,5]}, 
          ]

    def __str__(self):
        return f"Family Name: {self.last_name}, Members: {self._members})"


    # done
    def _generate_id(self):
        return randint(0, 99999999)


    # done
    def add_member(self, member):
        id_member = self._generate_id()
        last_name = self.last_name
        data = member
        data['id'] = id_member
        data['last_name'] = last_name
        self._members.insert(0, data)
  

    # done
    def delete_member(self, id):
        members = self._members
        
        for person in members:
            if person['id'] == id:
                members.remove(person)
                return members
        return 'No memeber for this is'


    # done
    def get_member(self, id):
        members = self._members
        
        for person in members:
            if person['id'] == id:
                return person
                
        return 'No memeber for this'


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members



# //////////////////////////////////////
# TESTING CLASS AND INSTANCES

# family = FamilyStructure("Garofalo")

# family.get_all_members()
# family.add_member('Lorenzo')
# family.add_member('Marco')
# family.add_member('Roberto')
# family.add_member('Gianna')
# family.add_member('Noah')
# family.add_member('Theo')
# family.add_member('Mary')