#include<QApplication>
#include<QWidget>

#include "main.moc"
#include<main.h>

MainWindow::MainWindow() {
    show();
}

int main(int argc, char** argv) {
    QApplication app = QApplication(argc, argv);
    MainWindow w;
    return app.exec();
}
