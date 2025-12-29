def main():
    dd, mm, aa = map(int, input().split('/'))
    
    print('%.2d/%.2d/%.2d' % (mm, dd, aa))
    print('%.2d/%.2d/%.2d' % (aa, mm, dd))
    print('%.2d-%.2d-%.2d' % (dd, mm, aa))
    
if __name__ == '__main__':
    main()
