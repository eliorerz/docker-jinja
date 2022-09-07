# python std lib
import sys

# docker_jinja3 package imports
from src.docker_jinja3 import cli


class TestCLI(object):
    def test_cli(self, tmpdir):
        """
        Test that when passing in certain arguments from commandline they
        are handled correctly by docopt and that the method creates a Core object
        and runs main method and the args dict passed in have correct format
        """
        dockerfile_input = tmpdir.join("Dockerfile.jinja")
        dockerfile_input.write("foobar")
        output = tmpdir.join("Dockerfile")
        dsfile = tmpdir.join("datasource.py")
        dsfile.write("#")

        sys.argv = [
            "scripts/dj",
            "-d",
            str(dockerfile_input),
            "-o",
            str(output),
            "-e",
            "OS=ubuntu:12.04",
            "-s",
            str(dsfile),
            "-vvvvv",
        ]

        expected = {
            "--dockerfile": str(dockerfile_input),
            "--env": ["OS=ubuntu:12.04"],
            "--help": False,
            "--outfile": str(output),
            "--quiet": False,
            "--verbosity": 5,
            "--version": False,
        }

        c = cli.main()

        for k, _ in expected.items():
            assert k in c.args

        assert str(dsfile) in c.args["--datasource"]
