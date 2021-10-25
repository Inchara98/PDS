import os

class directory():




    def get_config_ini_path(self):
        cwd = os.path.dirname(__file__)
        ini = os.path.join(cwd, 'Configurations/config.ini')
        return ini



    def get_sanity_testing_log_dir(self):
        cwd = os.path.dirname(__file__)
        log_dir_path = os.path.join(cwd, 'Screenshots/')
        return log_dir_path


