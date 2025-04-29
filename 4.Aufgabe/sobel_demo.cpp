#include<pybind11/pybind11.h>
#include<pybind11/numpy.h>
#include <pybind11/eigen.h>

namespace py = pybind11;


Eigen::MatrixXd sobel(Eigen::MatrixXd gray_img, Eigen::MatrixXd filter) {
    Eigen::MatrixXd filtered_img(gray_img.rows()-2, gray_img.cols()-2);
    
    // TODO: implement filter operation
    for (int y = 1; y < gray_img.rows() - 1; ++y) {
    for (int x = 1; x < gray_img.cols() - 1; ++x) {
        double value = 0.0;
        for (int j = -1; j <= 1; ++j) {
            for (int i = -1; i <= 1; ++i) {
                value += gray_img(y + j, x + i) * filter(j + 1, i + 1);
            }
        }
        filtered_img(y - 1, x - 1) = value;
    }
}

// Normalize output to 0–255
filtered_img = filtered_img.cwiseAbs(); // take absolute value
filtered_img = (filtered_img / filtered_img.maxCoeff()) * 255.0;


    return filtered_img;
}


PYBIND11_MODULE(sobel_demo, m) {
    m.doc() = "sobel operator using numpy!";
    m.def("sobel", &sobel);
}