import sqlite3
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException

class Sqlite_random(NeuronModule):

    def __init__(self, **kwargs):
        super(Sqlite_random, self).__init__(**kwargs)

        self.base = kwargs.get('base', None)
        self.table = kwargs.get('table', None)
        self.column = kwargs.get('column', None)

        # check if parameters have been provided
        if self._is_parameters_ok():

            conn = sqlite3.connect(self.base)

            command = "SELECT " + self.column +" from " + self.table + " ORDER BY random() LIMIT 1"

  	    cursor = conn.execute(command)

	    for row in cursor:
	        text = row[0]

	    conn.close()

	    self.message = {
	       "text": text
            }

	    self.say(self.message)

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise

        .. raises:: NotImplementedError
        """
        if self.base is None:
            raise MissingParameterException("Sqlite_random neuron needs a base location")
        if self.table is None:
            raise MissingParameterException("Sqlite_random neuron needs a table name")
        if self.column is None:
            raise MissingParameterException("Sqlite_random neuron needs a column name")

        return True