private static String b(WeakReference<Context> packageInfo) {
        packageInfo = packageInfo.get().getPackageManager().               getPackageInfo(packageInfo.get().getPackageName(),0);
        if (Build.VERSION.SDK_INT >= 9) {
            return "" + packageInfo.firstInstallTime + "-" + 
                            Math.abs(new Random().nextLong());
        }
        return UUID.randomUUID().toString();
    }
