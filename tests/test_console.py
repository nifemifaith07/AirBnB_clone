#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

HBNBCommand = console.HBNBCommand


class InstanceTest:
    """Class to store objects"""

    base = None
    amenity = None
    city = None
    place = None
    review = None
    state = None
    user = None
    created_instance_id = None


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def setUp(self) -> None:
        """Set up for console tests"""

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None, "console.py needs a docstring")
        self.assertTrue(
            len(console.__doc__) >= 1, "console.py needs a docstring"
        )

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(
            HBNBCommand.__doc__, None, "HBNBCommand class needs a docstring"
        )
        self.assertTrue(
            len(HBNBCommand.__doc__) >= 1,
            "HBNBCommand class needs a docstring"
        )


class TestConsoleCommands(unittest.TestCase):
    """Class for testing documentation of the console help command"""

    def test_help_command(self):
        """Test the help command"""
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("help")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Documented commands", output)

    def test_show_command(self):
        """Test the show command"""
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("help show")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("Print string rep of an instance 
                            based on classname and id", output)

    def test_create_command(self):
        """Test the create command"""
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("help create")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("Creates a new instance of BaseModel, saves it and prints the id", output)

    def test_update_command(self):
        """Test the update command"""
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("help update")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(
                "Updates instances based on the class name and id", output
            )

    def test_destroy_command(self):
        """Test the destroy command"""
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("help destroy")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("Destorys an instance that been passed", output)


class TestConsoleEOFCommand(unittest.TestCase):
    """Class for testing documentation of the console EOF command"""

    def test_eof_command(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("EOF")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("", output)

    def test_quit_command(self):
        """Test the quit command"""
        with patch("sys.exit") as mock_exit, patch(
            "sys.stdout", new=StringIO()
        ) as mock_stdout:
            console.HBNBCommand().onecmd("quit")

            # Check if sys.exit was called with the expected argument
            mock_exit.assert_called_once_with(1)
            # Check the output to confirm the help message
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")


class TestConsoleAllCommand(unittest.TestCase):
    """Class for testing documentation of the console all command"""

    def test_all_command_base_model(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            InstanceTest.base = BaseModel()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_all_command_amenity(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            InstanceTest.amenity = Amenity()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Amenity", output)

    def test_all_command_city(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            InstanceTest.city = City()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("City", output)

    def test_all_command_place(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            InstanceTest.place = Place()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Place", output)

    def test_all_command_review(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            InstanceTest.review = Review()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Review", output)

    def test_all_command_state(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            InstanceTest.state = State()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("State", output)

    def test_all_command_user(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            InstanceTest.user = User()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("User", output)

    def test_all_command_base_model_argument(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[BaseModel]", output)

    def test_all_command_amenity_argument(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all Amenity")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[Amenity]", output)

    def test_all_command_city_argument(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all City")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[City]", output)

    def test_all_command_place_argument(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all Place")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[Place]", output)

    def test_all_command_review_argument(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all Review")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[Review]", output)

    def test_all_command_state_argument(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all State")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[State]", output)

    def test_all_command_user_argument(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all User")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[User]", output)

    def test_all_command_invalid_argument(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all Base")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_all_instances_valid_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            # Create instances
            console.HBNBCommand().onecmd("create BaseModel")
            console.HBNBCommand().onecmd("create BaseModel")
            console.HBNBCommand().onecmd("create BaseModel")
            console.HBNBCommand().onecmd("all BaseModel")

            output = mock_stdout.getvalue().strip()
            self.assertEqual(len(output.split('\n')), 4)


class TestConsoleShowCommand(unittest.TestCase):
    """Class for testing documentation of the console show command"""

    def test_show_class_missing(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("show")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class name missing **", output)

    def test_show_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("show Base")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_show_base_model_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd(
                "show {}".format(InstanceTest.base.__class__.__name__)
            )
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** instance id missing **", output)

    def test_show_amenity_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd(
                "show {}".format(InstanceTest.amenity.__class__.__name__)
            )
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** instance id missing **", output)

    def test_show_city_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd(
                "show {}".format(InstanceTest.city.__class__.__name__)
            )
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** instance id missing **", output)

    def test_show_place_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd(
                "show {}".format(InstanceTest.place.__class__.__name__)
            )
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** instance id missing **", output)

    def test_show_review_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd(
                "show {}".format(InstanceTest.review.__class__.__name__)
            )
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** instance id missing **", output)

    def test_show_state_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd(
                "show {}".format(InstanceTest.state.__class__.__name__)
            )
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** instance id missing **", output)

    def test_show_user_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd(
                "show {}".format(InstanceTest.user.__class__.__name__)
            )
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** instance id missing **", output)

    def test_show_invalid_id(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd(
                "show BaseModel 49faff9a-6318-451f-87b6-910505c55907"
            )
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** no instance found **", output)


class TestConsoleCreateCommand(unittest.TestCase):
    """Class for testing documentation of the console create command"""

    def test_create_without_class_name(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("create")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class name missing **", output)

    def test_create_with_false_class_name(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("create Hamza")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_create_with_more_than_two_args(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("create BaseModel 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_create_without_class_name2(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("create()")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_create_with_false_class_name2(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("hamza.create()")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("*** Unknown syntax: hamza.create()", output)

    def test_create_and_show_instance(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("create BaseModel")
            create_output = mock_stdout.getvalue().strip()

            # Extracting the ID from the create output
            InstanceTest.created_instance_id = create_output.split()[-1]

            # Resetting the mock_stdout buffer
            mock_stdout.seek(0)
            mock_stdout.truncate(0)

            # Showing the created instance
            console.HBNBCommand().onecmd(
                f"show BaseModel {InstanceTest.created_instance_id}"
            )
            show_output = mock_stdout.getvalue().strip()

            self.assertIn(InstanceTest.created_instance_id, show_output)
            self.assertTrue("BaseModel" in show_output)


class TestConsoleUpdateCommand(unittest.TestCase):
    """Class for testing documentation of the console update command"""

    def test_update_without_class_name(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("update")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class name missing **", output)

    def test_update_with_false_class_name_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("update Hamza")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_update_with_false_id(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("update BaseModel 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** no instance found **", output)

    def test_update_without_class_name2(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("update()")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_update_with_false_class_name2(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("hamza.update()")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("*** Unknown syntax: hamza.update()", output)

    def test_update_and_show_instance(self):
        if InstanceTest.created_instance_id is not None:
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                console.HBNBCommand().onecmd(
                    "update BaseModel {} first_name \"Betty\"".format(
                        InstanceTest.created_instance_id)
                )

                # Resetting the mock_stdout buffer
                mock_stdout.seek(0)
                mock_stdout.truncate(0)

                # Showing the updated instance
                console.HBNBCommand().onecmd(
                    f"show BaseModel {InstanceTest.created_instance_id}"
                )

                show_output = mock_stdout.getvalue().strip()

                self.assertIn(InstanceTest.created_instance_id, show_output)
                self.assertTrue("BaseModel" in show_output)
                self.assertTrue("first_name" in show_output)
                self.assertTrue("Betty" in show_output)


class TestConsoleDeleteCommand(unittest.TestCase):
    """Class for testing documentation of the console delete command"""

    def test_destroy_without_class_name(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("destroy")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class name missing **", output)

    def test_destroy_with_false_class_name_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("destroy Hamza")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_destroy_with_false_id(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("destroy BaseModel 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** no instance found **", output)

    def test_destroy_without_class_name2(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("destroy()")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_destory_with_false_class_name2(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("hamza.destroy()")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("*** Unknown syntax: hamza.destroy()", output)

    def test_delete_and_show_instance(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd(
                "destroy BaseModel {}".format(
                    InstanceTest.created_instance_id)
            )

            # Resetting the mock_stdout buffer
            mock_stdout.seek(0)
            mock_stdout.truncate(0)

            # Showing the updated instance
            console.HBNBCommand().onecmd(
                f"show BaseModel {InstanceTest.created_instance_id}"
            )

            show_output = mock_stdout.getvalue().strip()
            self.assertNotIn(InstanceTest.created_instance_id, show_output)
            self.assertEqual("** no instance found **", show_output)

    def tearDown(self) -> None:
        InstanceTest.created_instance_id = None


if __name__ == "__main__":
    unittest.main()
