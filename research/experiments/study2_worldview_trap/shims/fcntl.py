"""No-op stand-in for the POSIX fcntl module, for running the BioSim MCP
server on Windows. The upstream recorder only calls flock() to keep the
driver and the MCP process from interleaving transcript lines; in this
driver only the MCP process writes the transcript while a watch is open."""

LOCK_SH = 1
LOCK_EX = 2
LOCK_NB = 4
LOCK_UN = 8


def flock(fd, operation):  # noqa: ARG001 - signature mirrors fcntl.flock
    return None
