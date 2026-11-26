# Maintainer: LOQ Vantage contributors
pkgname=loq-vantage
pkgver=0.1.0
pkgrel=3
pkgdesc="GTK4 control panel for Lenovo LOQ laptop hardware"
url="https://github.com/qiqifahreza/loq-vantage"
arch=('any')
license=('unknown')
depends=('gtk3' 'gtk4' 'libadwaita' 'libayatana-appindicator' 'polkit' 'python' 'python-gobject')
optdepends=('gnome-shell-extension-appindicator: show tray icon on GNOME Shell')
source=(
  'loq-vantage'
  'loq-vantage-tray'
  'loq-vantage-ctl'
  'loq-vantage.desktop'
  'com.lenovo.loqvantage.policy'
  '99-loq-vantage.rules'
  'loq-vantage.install'
  'loq-vantage.service'
  'loq-vantage.svg'
)
sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP')
install=loq-vantage.install

check() {
  cd "$startdir"
  python -m unittest discover -s tests -v
  printf '%s\n' "Tinjau aplikasi pada mode pratinjau; tutup jendelanya untuk melanjutkan instalasi."
  python "$startdir/loq-vantage" --preview
}

package() {
  install -Dm755 "$srcdir/loq-vantage" "$pkgdir/usr/bin/loq-vantage"
  install -Dm755 "$srcdir/loq-vantage-tray" "$pkgdir/usr/bin/loq-vantage-tray"
  install -Dm755 "$srcdir/loq-vantage-ctl" "$pkgdir/usr/bin/loq-vantage-ctl"
  install -Dm644 "$srcdir/loq-vantage.service" \
    "$pkgdir/usr/lib/systemd/user/loq-vantage.service"
  install -Dm644 "$srcdir/loq-vantage.svg" \
    "$pkgdir/usr/share/icons/hicolor/scalable/apps/loq-vantage.svg"
  install -Dm644 "$srcdir/loq-vantage.desktop" \
    "$pkgdir/usr/share/applications/loq-vantage.desktop"
  install -Dm644 "$srcdir/com.lenovo.loqvantage.policy" \
    "$pkgdir/usr/share/polkit-1/actions/com.lenovo.loqvantage.policy"
  install -Dm644 "$srcdir/99-loq-vantage.rules" \
    "$pkgdir/usr/lib/udev/rules.d/99-loq-vantage.rules"
}
