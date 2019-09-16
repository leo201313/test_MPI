from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [1,2,3]
    comm.send(data,dest=1,tag=11)

if rank == 1:
    atad = comm.recv(source=0,tag=11)
    print(atad)

