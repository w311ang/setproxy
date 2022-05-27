```yml
    - name: Set proxy
      uses: w311ang/setproxy@main
      with:
        config: ${{ secrets.ss_config }}
        password: ${{ secrets.frp_auth }}
        redirect: ${{ secrets.frp_redirect }}
```
