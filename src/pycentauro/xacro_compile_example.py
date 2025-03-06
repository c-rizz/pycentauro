from adarl.utils.utils import compile_xacro_string, pkgutil_get_path
from pathlib import Path

model_path = pkgutil_get_path("pycentauro","iit-centauro-ros-pkg/centauro_urdf/urdf/centauro.urdf.xacro")
urdf_string = compile_xacro_string( model_definition_string=Path(model_path).read_text(),
                                    model_kwargs={"realsense":"false",
                                                  "velodyne" :"false"},
                                    extra_pkg_paths={   "centauro_urdf" : pkgutil_get_path("iit-centauro-ros-pkg","centauro_urdf")})
print(urdf_string)