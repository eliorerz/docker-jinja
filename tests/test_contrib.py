# python std lib
import os

# docker_jinja3 package imports
from src.docker_jinja3.main import Core


class TestContribBasic(object):
    def test_env_var_is(self, tmpdir):
        dockerfile_input = tmpdir.join("Dockerfile.jinja")
        dockerfile_input.write("Key is set: {{ env_var_is('_foobar_', 'barfoo') }}")
        o = tmpdir.join("Dockerfile")

        c = Core(
            {
                "--dockerfile": str(dockerfile_input),
                "--outfile": str(o),
            }
        )
        c.main()
        assert o.read().startswith("Key is set: False")

        try:
            # Add key to environment and method should pick it up
            os.environ["_foobar_"] = "barfoo"
            c.main()
            assert o.read().startswith("Key is set: True")
        except Exception:
            raise
        finally:
            # Guaranteed cleanup of environment variable
            del os.environ["_foobar_"]


class TestContribFile(object):
    def test_file_exists(self, tmpdir):
        test_file = tmpdir.join("testfile.txt")
        test_file.write("foobar...")
        o = tmpdir.join("Dockerfile")
        input1 = tmpdir.join("Dockerfile1.jinja")
        input1.write("File exists: {{ file_exists('/tmp/foobar/barfoo/raboof') }}")

        c = Core(
            {
                "--dockerfile": str(input1),
                "--outfile": str(o),
            }
        )
        c.main()
        assert o.read().startswith("File exists: False"), f"{o.read()}"

        input2 = tmpdir.join("Dockerfile.jinja")
        input2.write("File exists: {{ file_exists('%s') }}" % str(test_file))  # noqa

        c = Core(
            {
                "--dockerfile": str(input2),
                "--outfile": str(o),
            }
        )
        c.main()

        assert o.read().startswith("File exists: True"), f"{o.read()}"
