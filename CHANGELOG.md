# Changelog

## 0.8.3

Update WhateverXe and [WhateverXe Graphics](https://github.com/b00t0x/WhateverXe-Graphics/releases) together.

### Added

- Add experimental VESA AUX brightness control for internal eDP on Alder Lake and Raptor Lake. Hardware validation on internal panels is pending.

### Fixed

- Improve experimental internal eDP support on Alder Lake and Raptor Lake at startup and after display sleep.
- Fix a GPU recovery failure that could stall a normal restart after a graphics hang.

## 0.8.2

Update WhateverXe and [WhateverXe Graphics](https://github.com/b00t0x/WhateverXe-Graphics/releases) together.

### Added

- Add support for Intel Raptor Lake-P Iris Xe Graphics (PCI Device IDs: `0xA7A0`, `0xA7A1`, `0xA7A8`, `0xA7A9`).
- Custom fork with 96 EU Raptor Lake-P enablement tested on 13th Gen Intel Core i9-13900H (Huawei MateBook D16).
- Experimental support for macOS Sequoia and macOS Tahoe.

## 0.8.1

Update WhateverXe and [WhateverXe Graphics](https://github.com/b00t0x/WhateverXe-Graphics/releases) together.

### Added

- Add experimental system sleep/wake support for internal displays and external displays connected before boot.
- Add experimental display sleep/wake support on modern external outputs.

### Fixed

- Improve internal display initialisation at boot.
