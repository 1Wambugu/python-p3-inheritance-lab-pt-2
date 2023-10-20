import io
import sys
from student import Student
from chatty_student import ChattyStudent

class TestStudent:
    def test_says_hello(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        student = Student()
        student.hello()
        sys.stdout = sys.__stdout__
        expected_output = "Hey there! I'm so excited to learn stuff.\n"
        assert captured_out.getvalue() == expected_output

    def test_raises_hand(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        student = Student()
        student.raise_hand()
        sys.stdout = sys.__stdout__
        expected_output = "Pick me!\n"
        assert captured_out.getvalue() == expected_output

class TestChattyStudent:
    def test_says_hello(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        chatty_student.hello()
        sys.stdout = sys.__stdout__
        expected_output = (
            "Hey there! I'm so excited to learn stuff.\n"
            "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...\n"
        )
        assert captured_out.getvalue() == expected_output

    def test_raises_hand(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        chatty_student.raise_hand()
        sys.stdout = sys.__stdout__
        expected_output = "Pick me!\n" * 10
        assert captured_out.getvalue() == expected_output
