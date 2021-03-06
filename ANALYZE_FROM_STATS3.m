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
npol=2%%%%%%%  CHANGE ME CAREFULLY: 1= pro_poor, 2=pro_rich, 3=random
%%%%%%%%%%%%%
pol(1).pol_id='pro poor';
pol(2).pol_id='pro rich';
pol(3).pol_id='random';
%%%%%%%%%%%%%
for ii= 1:3
    pol(ii).config.frac_edges = 0.1;
    pol(ii).config.frac_damage = 0.65;
    pol(ii).config.factor_reuse = 0.25;
    pol(ii).config.max_iterations = 270; %#300
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

pol(npol).p_l.p25=prctile(pol(npol).all_p_l',25);    pol(npol).std_imp.p25=prctile(pol(npol).all_std_imp',25);    pol(npol).mean_imp.p25=prctile(pol(npol).all_mean_imp',25);  pol(npol).n_kill.p25=prctile(pol(npol).all_n_kill',25);  pol(npol).tot_w.p25=prctile(pol(npol).all_tot_w',25);       
pol(npol).p_l.p75=prctile(pol(npol).all_p_l',75);    pol(npol).std_imp.p75=prctile(pol(npol).all_std_imp',75);    pol(npol).mean_imp.p75=prctile(pol(npol).all_mean_imp',75);  pol(npol).n_kill.p75=prctile(pol(npol).all_n_kill',75);   pol(npol).tot_w.p75=prctile(pol(npol).all_tot_w',75);     
pol(npol).p_l.avg=mean(pol(npol).all_p_l');          pol(npol).std_imp.avg=mean(pol(npol).all_std_imp');             pol(npol).mean_imp.avg=mean(pol(npol).all_mean_imp');         pol(npol).n_kill.avg=mean(pol(npol).all_n_kill');          pol(npol).tot_w.avg=mean(pol(npol).all_tot_w');          

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
%% make graphs variable (mean,25 and 75 percentile) x cycle
npol=2
max_num_steps= pol(npol).config.n_steps;
steps=[1:max_num_steps];

cols=[1,0,0; 0,0,1; 0,0,0];

figure(1);
p1=plot(steps,pol(npol).p_l.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).p_l.p25,'--','color',cols(npol,:)); hold on;
p3=plot(steps,pol(npol).p_l.p75,'--','color',cols(npol,:)); hold on;  
title('path length over cycles')
ylabel('path length'); xlabel('cycles');%legend([p1,p2,p3],'mean','pile25','pile75')
l1=plot(1,1,'color',cols(1,:)); hold on; l2=plot(1,1,'color',cols(2,:)); hold on; legend([l1,l2],'pro poor','pro rich')

figure(2);
p1=plot(steps,pol(npol).std_imp.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).std_imp.p25,'--','color',cols(npol,:)); hold on; 
p3=plot(steps,pol(npol).std_imp.p75,'--','color',cols(npol,:)); hold on;  
title('stand deviation of the importance of the edges over the cycles');
ylabel('std dev of edge importance'); xlabel('cycles');% legend([p1,p2,p3],'mean','pile25','pile75')
l1=plot(1,1,'color',cols(1,:)); hold on; l2=plot(1,1,'color',cols(2,:)); hold on; legend([l1,l2],'pro poor','pro rich')

figure(3);
p1=plot(steps,pol(npol).mean_imp.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).mean_imp.p25,'--','color',cols(npol,:)); hold on; 
p3=plot(steps,pol(npol).mean_imp.p75,'--','color',cols(npol,:)); hold on;  
title('mean edge importance over cycles')
ylabel('mean edge importance'); xlabel('cycles');%legend([p1,p2,p3],'mean','pile25','pile75')
l1=plot(1,1,'color',cols(1,:)); hold on; l2=plot(1,1,'color',cols(2,:)); hold on; legend([l1,l2],'pro poor','pro rich')

figure(4);
p1=plot(steps,pol(npol).n_kill.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).n_kill.p25,'--','color',cols(npol,:)); hold on; 
p3=plot(steps,pol(npol).n_kill.p75,'--','color',cols(npol,:)); hold on;  
title('number of dead edges over cycles')
ylabel('number of dead edges '); xlabel('cycles');%legend([p1,p2,p3],'mean','pile25','pile75')
l1=plot(1,1,'color',cols(1,:)); hold on; l2=plot(1,1,'color',cols(2,:)); hold on; legend([l1,l2],'pro poor','pro rich')

figure(5);
p1=plot(steps,pol(npol).tot_w.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).tot_w.p25,'--','color',cols(npol,:)); hold on;
p3=plot(steps,pol(npol).tot_w.p75,'--','color',cols(npol,:)); hold on;
title('total weight of the graph over cycles')
ylabel('total weight of the graph'); xlabel('cycles');%legend([p1,p2,p3],'mean','pile25','pile75');
l1=plot(1,1,'color',cols(1,:)); hold on; l2=plot(1,1,'color',cols(2,:)); hold on; legend([l1,l2],'pro poor','pro rich')

adjustallplots(4,4)
%% make cumulative of killed edges x cycle

figure(6); hold on;
p1=plot(steps,cumsum(pol(npol).n_kill.avg),'color',cols(npol,:)); hold on;
p2=plot(steps,(pol(npol).n_kill.p25),'--','color',cols(npol,:)); hold on;
p3=plot(steps,cumsum(pol(npol).n_kill.p75),'--','color',cols(npol,:)); hold on;  
title('cumulative number of dead edges over cycles')
ylabel('cumulative number of dead edges '); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')


%% semilog plots
figure; subplot(2,3,1); semilogy(steps,pol(1).p_l.avg,'r');hold on; semilogy(steps,pol(2).p_l.avg);  ylabel('path length'); xlabel('cycles');
subplot(2,3,2); semilogy(steps,pol(1).tot_w.avg,'r');hold on; semilogy(steps,pol(2).tot_w.avg);      ylabel('total weight'); xlabel('cycles');
subplot(2,3,3); semilogy(steps,pol(1).n_kill.avg,'r');hold on; semilogy(steps,pol(2).n_kill.avg);    ylabel('number of dead edges'); xlabel('cycles');
subplot(2,3,4); semilogy(steps,pol(1).mean_imp.avg,'r');hold on; semilogy(steps,pol(2).mean_imp.avg);ylabel('mean importance'); xlabel('cycles');
subplot(2,3,5); semilogy(steps,pol(1).std_imp.avg,'r');hold on; semilogy(steps,pol(2).std_imp.avg);  ylabel('std dev of importance'); xlabel('cycles');
l1=plot(1,1,'color',cols(1,:)); hold on; l2=plot(1,1,'color',cols(2,:)); hold on; legend([l1,l2],'pro poor','pro rich')

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

cols=winter(5);
figure; p1=plot(steps,flatw./max(flatw),'color',cols(1,:));hold on; p2=plot(steps,flatpl./max(flatpl),'color',cols(2,:));hold on; 
p3=plot(steps,flatsti./max(flatsti),'color',cols(3,:));hold on;
p4=plot(steps,flatk./max(flatk),'color',cols(4,:));hold on; p5=plot(steps,flatmi./max(flatmi),'color',cols(5,:));
legend([p1,p2,p3,p4,p5],'total weight','path length','std dev importance','num killed', 'mean importance')
title('where it is interesting to do a fit?');

%% 
minval2fit=1;
maxval2fit=length(steps);%200;% length(steps)
goodsteps=minval2fit:maxval2fit;
pol(npol).tofit.goodsteps=goodsteps;
pol(npol).tofit.all_p_l=pol(npol).all_p_l(goodsteps,:); pol(npol).tofit.all_std_imp=pol(npol).all_std_imp(goodsteps,:); pol(npol).tofit.all_mean_imp=pol(npol).all_mean_imp(goodsteps,:);
pol(npol).tofit.all_n_kill=pol(npol).all_n_kill(goodsteps,:); pol(npol).tofit.all_tot_w=pol(npol).all_tot_w(goodsteps,:);


%%  curve fitting
cftool(steps,log(pol(npol).p_l.avg)) % generated:

[fitresult, gof] = createexpFit(steps(goodsteps),pol(npol).p_l.avg(goodsteps),'path length','exp')
[fitresult, gof] = createexpFit(steps,pol(npol).tot_w.avg,'total graph weight','exp')
[fitresult, gof] = createexpFit(steps,pol(npol).std_imp.avg,'std dev of edges importance','gauss')
[fitresult, gof] = createexpFit(log(steps),pol(npol).n_kill.avg,'std dev of edges importance','gauss')

cftool(steps,pol(npol).tot_w.avg) % generated:

%% a detailed graph

npol=2
cols=[0,0,1; 1,0,0; 0,0,0];

figure(1);
b1=plot(steps,pol(1).p_l.avg,'color',cols(1,:)); hold on;
b2=plot(steps,pol(1).p_l.p25,'--','color',cols(1,:)); hold on;
b3=plot(steps,pol(1).p_l.p75,'--','color',cols(1,:)); hold on; 

r1=plot(steps,pol(2).p_l.avg,'color',cols(2,:)); hold on;
r2=plot(steps,pol(2).p_l.p25,'--','color',cols(2,:)); hold on;
r3=plot(steps,pol(2).p_l.p75,'--','color',cols(2,:)); hold on; 
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