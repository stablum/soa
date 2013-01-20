% IMPORT_FROM_STATS
% drag & drop stats. import as column vectors
%---------------------------------
% countsteps ---> countinterations
% expnum ---> runnum
% meanedgesimportance
% stdedgesimportance
% numkills
% pathlength
% totalweight
%----------------------------------

% from columns to matrix using steps and expnum: rows=RUNS, columns=exp
% for each variable, take mean and 25/75%iles of each cycle
% make graphs var vs cycle
% make anova of [final] values
%----------------------------------
%% from columns to matrix using steps and runnum: rows=RUNS, columns=exp
runnum=runnum+1; % DO Once, better to FIX BEFORE
countiterations=countiterations+1;
%% PUT everything under the correct policy structure.
%%%%%%%%%%%%%
npol=1%%%%%%%  CHANGE ME CAREFULLY: 1= pro_poor, 2=pro_rich, 3=random
%%%%%%%%%%%%%
pol(1).pol_id='pro poor';
pol(2).pol_id='pro rich';
pol(3).pol_id='random';
%%%%%%%%%%%%%
for ii= 1:3
    pol(ii).config.frac_edges = 0.1;
    pol(ii).config.frac_damage = 0.65;
    pol(ii).config.factor_reuse = 0.25;
    pol(ii).config.treshold_kill = 0.2;
end
pol(npol).config.n_steps=max(countiterations);
pol(npol).comfig.n_runs=max(runnum);
%%
max_num_steps= pol(npol).config.n_steps;
max_num_runs= pol(npol).comfig.n_runs;
steps=[1:max_num_steps];
runs=[1:max_num_runs];
ss=0;
pol(npol).all_steps=[];pol(npol).all_p_l=[];pol(npol).all_std_imp=[];pol(npol).all_mean_imp=[];pol(npol).all_n_kill=[];pol(npol).all_tot_w=[];
for col= runs
    for row=steps
        ss=ss+1;
            pol(npol).all_p_l(row,col)=pathlength(ss);
            pol(npol).all_std_imp(row,col)=stdedgesimportance(ss);
            pol(npol).all_mean_imp(row,col)=meanedgesimportance(ss);
            pol(npol).all_n_kill(row,col)=numkills(ss);
            pol(npol).all_tot_w(row,col)=totalweight(ss);
            pol(npol).all_steps(row,col)=countiterations(ss);
    end
end
%% for each variable, take mean and 25/75%iles of each cycle
pol(npol).p_l.p5=prctile(pol(npol).all_p_l',5);      pol(npol).std_imp.p5=prctile(pol(npol).all_std_imp',5);      pol(npol).mean_imp.p5=prctile(pol(npol).all_mean_imp',5);  pol(npol).n_kill.p5=prctile(pol(npol).all_n_kill',5);  pol(npol).tot_w.p5=prctile(pol(npol).all_tot_w',5);       
pol(npol).p_l.p25=prctile(pol(npol).all_p_l',25);    pol(npol).std_imp.p25=prctile(pol(npol).all_std_imp',25);    pol(npol).mean_imp.p25=prctile(pol(npol).all_mean_imp',25);  pol(npol).n_kill.p25=prctile(pol(npol).all_n_kill',25);  pol(npol).tot_w.p25=prctile(pol(npol).all_tot_w',25);       
pol(npol).p_l.p75=prctile(pol(npol).all_p_l',75);    pol(npol).std_imp.p75=prctile(pol(npol).all_std_imp',75);    pol(npol).mean_imp.p75=prctile(pol(npol).all_mean_imp',75);  pol(npol).n_kill.p75=prctile(pol(npol).all_n_kill',75);   pol(npol).tot_w.p75=prctile(pol(npol).all_tot_w',75);     
pol(npol).p_l.p95=prctile(pol(npol).all_p_l',95);    pol(npol).std_imp.p95=prctile(pol(npol).all_std_imp',95);    pol(npol).mean_imp.p95=prctile(pol(npol).all_mean_imp',95);  pol(npol).n_kill.p95=prctile(pol(npol).all_n_kill',95);  pol(npol).tot_w.p95=prctile(pol(npol).all_tot_w',95);       

pol(npol).p_l.avg=mean(pol(npol).all_p_l');          pol(npol).std_imp.avg=mean(pol(npol).all_std_imp');          pol(npol).mean_imp.avg=mean(pol(npol).all_mean_imp');         pol(npol).n_kill.avg=mean(pol(npol).all_n_kill');          pol(npol).tot_w.avg=mean(pol(npol).all_tot_w');          
pol(npol).p_l.med=median(pol(npol).all_p_l');        pol(npol).std_imp.med=median(pol(npol).all_std_imp');        pol(npol).mean_imp.med=median(pol(npol).all_mean_imp');         pol(npol).n_kill.med=median(pol(npol).all_n_kill');          pol(npol).tot_w.med=median(pol(npol).all_tot_w');          

%% SAVE
%%%%%%%%%%%
mypath='D:\ELECTIVES\SELF_ORGA\ad_code_versions\300 cycle\';
myfile='polstats.mat';
save([mypath,myfile],'pol')
%%%%%%%%%%%
%% LOAD
%%%%%%%%%%%
mypath='D:\ELECTIVES\SELF_ORGA\ad_code_versions\300 cycle\';
myfile='polstats.mat';
load([mypath,myfile],'pol')
%%%%%%%%%%%
%% make plots variable (mean,25 and 75 percentile) x cycle
for pp=1:3
    plot_var2cycles(pp,pol)
end
%% make conf interval plots
vars={'p_l'; 'n_kill';'tot_w'; 'std_imp';'mean_imp'; };
namevars={'path length'; 'number of dead edges'; 'total weight of the graph'; 'sted dev of importance'; 'mean importance'};
for vv=1:5
    var=vars{vv}; namevar=vars{vv};
    mtplotciGE(pol,var,namevar);
end
%% make cumulative of killed edges x cycle

figure(6); hold on;
p1=plot(steps,cumsum(pol(npol).n_kill.avg),'color',mycols(npol,:)); hold on;
p2=plot(steps,(pol(npol).n_kill.p25),'--','color',mycols(npol,:)); hold on;
p3=plot(steps,cumsum(pol(npol).n_kill.p75),'--','color',mycols(npol,:)); hold on;  
title('cumulative number of dead edges over cycles')
ylabel('cumulative number of dead edges '); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

%% semilog plots
for pp=1:3
    plot_semilog2cycles(pp,pol)
end
%% which interval deserves to be fitted?
[flatw]=checkflat(pol(npol).tot_w.avg);
figure; plot(steps,pol(npol).tot_w.avg); hold on;plot(steps,flatw,'r') 
[flatpl]=checkflat(pol(npol).p_l.avg);
figure; plot(steps,pol(npol).p_l.avg); hold on; plot(steps,flatpl,'r'); 
[flatsti]=checkflat(pol(npol).std_imp.avg);
figure; plot(steps,pol(npol).std_imp.avg); hold on;plot(steps,flatsti,'r') 
[flatk]=checkflat(pol(npol).n_kill.avg);
figure; plot(steps,pol(npol).n_kill.avg); hold on; plot(steps,flatk,'r');  
[flatmi]=checkflat(pol(npol).mean_imp.avg);
figure; plot(steps,pol(npol).mean_imp.avg); hold on; plot(steps,flatmi,'r');

mycols=winter(5);
figure; p1=plot(steps,flatw./max(flatw),'color',mycols(1,:));hold on; p2=plot(steps,flatpl./max(flatpl),'color',mycols(2,:));hold on; 
p3=plot(steps,flatsti./max(flatsti),'color',mycols(3,:));hold on;
p4=plot(steps,flatk./max(flatk),'color',mycols(4,:));hold on; p5=plot(steps,flatmi./max(flatmi),'color',mycols(5,:));
legend([p1,p2,p3,p4,p5],'total weight','path length','std dev importance','num killed', 'mean importance')
title('where it is interesting to do a fit?');

%% select only some steps to be fit
max_num_steps= pol(npol).config.n_steps;
steps=[1:max_num_steps];
minval2fit=1;
maxval2fit=200;%length(steps);%% length(steps)
goodsteps=minval2fit:maxval2fit;
pol(npol).tofit.goodsteps=goodsteps;
pol(npol).tofit.all_p_l=pol(npol).all_p_l(goodsteps,:); pol(npol).tofit.all_std_imp=pol(npol).all_std_imp(goodsteps,:); pol(npol).tofit.all_mean_imp=pol(npol).all_mean_imp(goodsteps,:);
pol(npol).tofit.all_n_kill=pol(npol).all_n_kill(goodsteps,:); pol(npol).tofit.all_tot_w=pol(npol).all_tot_w(goodsteps,:);


%%  try out some curve fitting on avg signal
npol=3
cftool(steps(goodsteps),log(pol(npol).p_l.avg(goodsteps))) % generated:
%% do the curve fitting on avg signal
 plot_exponential_fit;
%% fit with wbl
myweibulfit( pol,myvar)
%%
figure
pp=1
goodsteps=1:260;
xx=log(nonzeros(pol(pp).p_l.avg(goodsteps)));
x=xx+abs(min(xx))+0.1; % shift it pos
wblplot(x)

 PD = fitdist(x, 'wbl')
 [h, p, ksstat, cv]=kstest(x,PD)%,alpha, type

  PD = fitdist(x, 'exp')
 [h, p, ksstat, cv]=kstest(x,PD)%,alpha, type
 
% a=PD.Params(1);
% b=PD.Params(2);
[p,ci] = wblfit(x) %;%gamfit(x)
Y = gampdf(x,p(1),p(2))
figure; subplot(2,1,1); plot([1:length(x)],x); hold on; plot([1:length(Y)],Y,'r');
subplot(2,1,2); plot(x,Y);
% check nice distrib
disttool
% fit data to dist
dfittool(x)
% test the goodness of dist
[p,ci] = wblfit(x)
[ProbDist] = wblcdf(x,p(1),p(2));
cdf=ProbDist;
[h, p, ksstat, cv]=kstest(x,cdf)%,alpha, type

% nonlinear fit
xx=steps(goodsteps);
yy=(pol(pp).n_kill.avg(goodsteps));
modelFun =  @(p,x) p(3) .* (x ./ p(1)).^(p(2)-1) .* exp(-(x ./ p(1)).^p(2));
startingVals = [200 20 50];% xcenter ycenter % xscale shape yscale
coefEsts = nlinfit(xx, yy, modelFun, startingVals);

figure;
plot(xx,yy,'o'); hold on;
xgrid = linspace(0,20,100);
line(xgrid, modelFun(coefEsts, xgrid), 'Color','r');
%

[p,ci] = wblfit(x);
%
% http://www.mathworks.nl/products/statistics/examples.html?file=/products/demos/shipping/stats/cfitdfitdemo.html#1
cftool(steps,pol(npol).tot_w.avg) % generated:
%% plot parameters of fitting
plot([1,1,1],[a0 a2],'color',cols(npol,:),')
%% a detailed graph

npol=2
mycols=[0,0,1; 1,0,0; 0,0,0];

figure(1);
b1=plot(steps,pol(1).p_l.avg,'color',mycols(1,:)); hold on;
b2=plot(steps,pol(1).p_l.p25,'--','color',mycols(1,:)); hold on;
b3=plot(steps,pol(1).p_l.p75,'--','color',mycols(1,:)); hold on; 

r1=plot(steps,pol(2).p_l.avg,'color',mycols(2,:)); hold on;
r2=plot(steps,pol(2).p_l.p25,'--','color',mycols(2,:)); hold on;
r3=plot(steps,pol(2).p_l.p75,'--','color',mycols(2,:)); hold on; 
title('path length over cycles')
ylabel('path length'); xlabel('cycles');legend([b1,b2,b3],'mean','pile25','pile75');
legend([b1,r1],'pro poor','pro rich')

%% make anova of [final] values



countsteps

runnum

meanedgesimportance

stdedgesimportance

numkills

pathlength

totalweight