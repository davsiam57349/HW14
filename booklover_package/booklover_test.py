import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        david = BookLover("david", "david@david.dav", "nonfic")
        david.add_book("Magic Tree House 3", 5)
        self.assertTrue("Magic Tree House 3" in david.book_list['book_name'].unique())

    def test_2_add_book(self):
        joe = BookLover("joe", "joe@joe.edu", "fic")
        joe.add_book("Magic Tree House 4", 4)
        joe.add_book("Magic Tree House 4", 3)
        self.assertTrue(len(joe.book_list) == 1)

    def test_3_has_read(self): 
        doug = BookLover("doug", "doug@doug.doug", "fanfic")
        doug.add_book("Magic Tree House 2", 2)
        self.assertTrue(doug.has_read("Magic Tree House 2"))
    
    def test_4_has_read(self): 
        norbert = BookLover("norbert", "norbert@norb.norb", "biographies")
        norbert.add_book("Magic Tree House 7", 1)
        self.assertFalse(norbert.has_read("Magic Tree House 3"))

    def test_5_num_books_read(self): 
        clarence = BookLover("clarence", "clarence@clarence", "cookbooks")
        clarence.add_book("Magic Tree House 30", 3)
        clarence.add_book("Magic Tree House 31", 1)
        clarence.add_book("Magic Tree House 32", 5)
        clarence.add_book("Magic Tree House 33", 1)
        clarence.add_book("Magic Tree House 34", 4)
        self.assertEqual(clarence.num_books_read(), 5)

    def test_6_fav_books(self):
        jermichael = BookLover("jermichael", "jermichael@virginia.edu", "sci fi")
        jermichael.add_book("Magic Tree House 35", 4)
        jermichael.add_book("Magic Tree House 36", 1)
        jermichael.add_book("Magic Tree House 37", 2)
        jermichael.add_book("Magic Tree House 38", 5)
        jermichael.add_book("Magic Tree House 39", 3)
        fav_ratings = jermichael.fav_books()["book_rating"]
        for i in fav_ratings:
            self.assertTrue(i > 3)

        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3


if __name__ == '__main__':

    unittest.main(verbosity=3)