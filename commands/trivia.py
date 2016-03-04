from commands.command import Command


class TriviaCommand(Command):

    def __init__(self, trivia_question_repository, user_repository):
        Command.__init__(self)

        self._trivia_question_repository = trivia_question_repository
        self._user_repository = user_repository
        self._game_started = False
        self._current_question = None

    def execute(self, channel, parameters):
        if len(parameters) == 0:
            channel.send_message("Usage: !trivia [answer, !startgame, !endgame, !current or !skip]")

        if self._game_started:
            self.__handle_game_command__(channel, parameters)
        else:
            self.__handle_command__(channel, parameters)

    def __handle_game_command__(self, channel, parameters):
        if len(parameters) == 1 and parameters[0][0] == "!":
            if parameters[0] == "!current":
                channel.send_message(self._current_question)
            elif parameters[0] == "!skip":
                self.__get_trivia_question__()
                self.__show_current_question__(channel)
            elif parameters[0] == "!endgame":
                channel.send_message("GAME OVER")
                self._game_started = False
                self._current_question = None
        else:
            answer = " ".join(parameters)
            if self._current_question.answer.lower() == answer.lower():
                channel.send_message("CORRECT!!!")
                self.__get_trivia_question__()
                self.__show_current_question__(channel)
            else:
                channel.send_message("Nope!")

    def __handle_command__(self, channel, parameters):
        if len(parameters) == 1 and parameters[0] == "!startgame":
            self.__get_trivia_question__()
            self._game_started = True

            channel.send_message("Starting a new game of trivia, hold on to your dicks!")
            self.__show_current_question__(channel)

    def __get_trivia_question__(self):
        self._current_question = self._trivia_question_repository.random()

    def __show_current_question__(self, channel):
        channel.send_message("#{} - {}".format(self._current_question.entity_id, self._current_question.question))
