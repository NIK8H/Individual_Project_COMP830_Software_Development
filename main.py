class QuestionNode:
    def __init__(self, question):
        self.question = question
        self.yes = None
        self.no = None

    def set_yes_question(self, yes):
        self.yes = yes

    def set_no_question(self, no):
        self.no = no


class GameTree:
    def __init__(self, root):
        self.current_node = self.root = root

    def start(self):
        while self.current_node:
            print(self.current_node.question)
            answer = self.read_input()
            if answer.lower() == "yes":
                self.answer_yes()
            else:
                self.answer_no()

    def answer_yes(self):
        self.current_node = self.current_node.yes

    def answer_no(self):
        self.current_node = self.current_node.no

    def read_input(self):
        return input()


start_game = QuestionNode("Welcome to the game! Think of a design pattern and answer as yes or no. Ready?")
is_flexible = QuestionNode(
    "Does it provide the object creation mechanism that enhance the flexibilites of the existing code?")
is_single_instance = QuestionNode("Does it ensure you have at most one instance of a class in your application?")
is_singleton_pattern = QuestionNode("Is it Singleton Pattern?")
is_builder_pattern = QuestionNode("Is it builder pattern?")
is_communication = QuestionNode("Is it responsible for how one class communicates with other?")
is_behavior = QuestionNode("Does it provide a mechanism to the context to change its behavior?")
is_behavior_scheme = QuestionNode("Is changing behavior built into its scheme?")
is_notify_group = QuestionNode("Does it allow a group of objects to be notifed when some state changes?")
is_state_pattern = QuestionNode("Is it state pattern?")
is_strategy_pattern = QuestionNode("Is it Strategy pattern?")
is_observer_pattern = QuestionNode("Is it observer pattern?")
is_command_pattern = QuestionNode("Is it command pattern?")
is_relation = QuestionNode(
    "Does it explain how to assemble objects and classes into a larger structure and simplifies structure by identifying the relationships?")
is_dynamic = QuestionNode("Does it attach additional behavior to an object dynamically at run-time?")
is_decorator_pattern = QuestionNode("Is it decorator pattern?")
is_adapter_pattern = QuestionNode("Is it adapter pattern?")
is_correct = QuestionNode("Wohoo! I guessed it! Try again?")
is_wrong = QuestionNode("Oops! Something went wrong! Try again?")

start_game.set_yes_question(is_flexible)
start_game.set_no_question(is_wrong)
is_correct.set_yes_question(start_game)
is_wrong.set_yes_question(start_game)
is_flexible.set_yes_question(is_single_instance)
is_flexible.set_no_question(is_communication)
is_single_instance.set_yes_question(is_singleton_pattern)
is_single_instance.set_no_question(is_builder_pattern)
is_communication.set_yes_question(is_behavior)
is_communication.set_no_question(is_relation)
is_behavior.set_yes_question(is_behavior_scheme)
is_behavior.set_no_question(is_notify_group)
is_behavior_scheme.set_yes_question(is_state_pattern)
is_behavior_scheme.set_no_question(is_strategy_pattern)
is_notify_group.set_yes_question(is_observer_pattern)
is_notify_group.set_no_question(is_command_pattern)
is_relation.set_yes_question(is_dynamic)
is_relation.set_no_question(is_wrong)

is_dynamic.set_yes_question(is_decorator_pattern)
is_dynamic.set_no_question(is_adapter_pattern)


def set_leaf_node(pattern):
    pattern.set_yes_question(is_correct)
    pattern.set_no_question(is_wrong)


set_leaf_node(is_decorator_pattern)
set_leaf_node(is_adapter_pattern)
set_leaf_node(is_observer_pattern)
set_leaf_node(is_command_pattern)
set_leaf_node(is_strategy_pattern)
set_leaf_node(is_singleton_pattern)
set_leaf_node(is_builder_pattern)

def main():
    game = GameTree(start_game)
    game.start()

if __name__ == '__main__':
    main()

