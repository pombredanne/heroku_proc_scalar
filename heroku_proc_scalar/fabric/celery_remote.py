from fabric.api import task
from heroku_proc_scalar.utils import shutdown_celery_processes, start_dynos, get_running_celery_workers, lock_celery, unlock_celery


@task
def unlock_after_deployment():
    return unlock_celery()


@task
def lock_for_deployment():
    return lock_celery()


@task
def shutdown_process(*worker_hostnames):

    return shutdown_celery_processes(worker_hostnames)


@task
def shutdown_process_for_deployment():

    return shutdown_celery_processes([], 'deployment')


@task
def restart_processes(*worker_hostnames):

    return start_dynos(worker_hostnames)


@task
def restart_processes_after_deployment(*worker_hostnames):

    return start_dynos(worker_hostnames, 'deployment')


@task
def print_running_processes():

    proclist = get_running_celery_workers()
    list = ",".join(proclist)

    print "PROCLIST={0}".format(list)
