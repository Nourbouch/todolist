# Maintainer: Nour bouch <https://github.com/Nourbouch>
pkgname=todo-manager
pkgver=1.0.0
pkgrel=1
pkgdesc="A simple TODO list manager with a GUI"
arch=('any')
url="https://localhost"
license=('MIT')
depends=('python' 'tk' 'python-reportlab')
source=("src/main.py")
sha256sums=('SKIP')

package() {
    install -Dm755 "$srcdir/main.py" "$pkgdir/usr/bin/todo-manager"
}
