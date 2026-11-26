# Maintainer: LOQ Vantage contributors
pkgname=loq-vantage
pkgver=0.1.0
pkgrel=2
pkgdesc="GTK4 control panel for Lenovo LOQ laptop hardware"
arch=('any')
license=('unknown')
depends=('gtk4' 'libadwaita' 'polkit' 'python' 'python-gobject')
source=(
  'loq-vantage'
  'loq-vantage-ctl'
  'loq-vantage.desktop'
  'com.lenovo.loqvantage.policy'
  '99-loq-vantage.rules'
  'loq-vantage.install'
)
sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP')
install=loq-vantage.install

package() {
  install -Dm755 "$srcdir/loq-vantage" "$pkgdir/usr/bin/loq-vantage"
  install -Dm755 "$srcdir/loq-vantage-ctl" "$pkgdir/usr/bin/loq-vantage-ctl"
  install -Dm644 "$srcdir/loq-vantage.desktop" \
    "$pkgdir/usr/share/applications/loq-vantage.desktop"
  install -Dm644 "$srcdir/com.lenovo.loqvantage.policy" \
    "$pkgdir/usr/share/polkit-1/actions/com.lenovo.loqvantage.policy"
  install -Dm644 "$srcdir/99-loq-vantage.rules" \
    "$pkgdir/usr/lib/udev/rules.d/99-loq-vantage.rules"
}
