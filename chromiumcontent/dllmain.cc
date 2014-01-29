#if defined(WIN32)
#include <windows.h>

BOOL WINAPI DllMain(HINSTANCE hInstDll, DWORD fdwReason, LPVOID lpvReserved) {
  return TRUE;
}
#endif
