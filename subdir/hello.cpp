// 2026-05-24
#include <iostream>
#include <ctime>

int main()
{
    std::cout << "Hello World !!" << std::endl;
    std::time_t now = std::time(nullptr);
    std::tm *tm_now = std::localtime(&now);
    if (tm_now != nullptr) {
        char datetime[20];
        if (std::strftime(datetime, sizeof(datetime), "%Y-%m-%d %H:%M:%S", tm_now) > 0) {
            std::cout << datetime << std::endl;
        } else {
            std::cout << "none" << std::endl;
        }
    } else {
        std::cout << "none" << std::endl;
    }
    return 0;
}
