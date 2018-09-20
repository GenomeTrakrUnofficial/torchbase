def get_database_state(database, state=None):
	"check if the state is a valid state for the database, or get the most recent state and return it"
	if state:
		return state
	return 'd41d8cd98f00b204e9800998ecf8427e'