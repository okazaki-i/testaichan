// 2026-05-24
#include <iostream>
#include <ctime>

int main()
{
    std::cout << "Hello world" << std::endl;
    std::time_t now = std::time(nullptr);
    std::tm *tm_now = std::localtime(&now);
    if (tm_now != nullptr) {
        char date[11];
        if (std::strftime(date, sizeof(date), "%Y-%m-%d", tm_now) > 0) {
            std::cout << date << std::endl;
        } else {
            std::cout << "none" << std::endl;
        }
    } else {
        std::cout << "none" << std::endl;
    }
    return 0;
}
