"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
             {
                "id": self._generate_id(),
                "first_name": "francisco",
                "last_name": last_name,
                "age": 37,
                "lucky_numbers": [9, 36, 99]
            },
            {
                "id": self._generate_id(),
                "first_name": "pedro",
                "last_name": last_name,
                "age": 18,
                "lucky_numbers": [4, 10, 5]
            }

        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
    def _paslastname(self):
        ## pasa el lastname
        return  self.last_name
    def add_member(self, member):
        ## You have to implement this method
        ## Append the member to the list of _members
        self._members.append(member)
        return self._members
        

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        for i in range(0, len(self._members)):
             if (self._members[i]["id"] == int(id)):
                 del self._members[i]
                 body = {"done":True}
                 break
        return  body

    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        person = list(filter(lambda item:item["id"] == int(id),self._members))
        return person 

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    

    